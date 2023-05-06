window.onload = () => {
    reset_placeholders();
}

// calls flask backend, passing in asm input from textarea to our CGenerator
// if successful, takes generated C code and displays it 
const decompile = () => {
    const asm_code = document.getElementById('asm-input').value;
    const url = window.location.href + 'decompile';
    console.log(asm_code);
    setup_placeholders();

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(asm_code)
    })
    .then(response => response.json())
    .then(data => display_translation(data))
    .catch(error => {
        reset_placeholders();
        alert(error);
        console.log(error);
    });
}

// calls flask backend, randomly selecting a short ASM snippet from our data folder
// if successful, displays this selected ASM snippet 
const randomize = () => {
    const url = window.location.href + 'randomize';

    fetch(url)
        .then(response => response.json())
        .then(data => display_randomized(data))
        .catch(error => {
            reset_placeholders();
            alert(error);
            console.log(error);
    }); 
}

// display translated asm!
const display_translation = (c_output) => {
    // c_output is translated asm code as one string
    console.log(c_output);

    reset_placeholders();
    document.getElementById('c-output').value = c_output;
    // can style or print token by token, but for now, just write all
    // let x = 0;
    // for (token of c_output.split(' ')) {   
    //     setTimeout(() => {document.getElementById('c-output').value += token + ' '}, x);
    //     x += 500;
    // }
}

// display randomized asm!
const display_randomized = (random_asm) => {
    document.getElementById('asm-input').value = random_asm;
}

// hide loader and reset C output textarea placeholder to default func
const reset_placeholders = () => {
    document.getElementById('loader').classList.add('hidden');
    document.getElementById('c-output').setAttribute('placeholder', 'int f() {\n\treturn 0;\n}');
}

// start loader and clear C output textarea placeholder + existing code
const setup_placeholders = () => {
    document.getElementById('c-output').setAttribute('placeholder', '');
    document.getElementById('loader').classList.remove('hidden');
    document.getElementById('c-output').value = '';
}