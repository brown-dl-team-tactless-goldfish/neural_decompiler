window.onload = () => {
    document.getElementById('c-output').setAttribute('placeholder', 'int f() {\n\treturn 0;\n}');
}

const decompile = () => {
    const asm_code = document.getElementById('asm-input').value;
    console.log(asm_code);
    document.getElementById('c-output').value = '';
    document.getElementById('c-output').setAttribute('placeholder', '');
    document.getElementById('loader').classList.remove('hidden');

    const url = window.location.href + 'decompile?asm_code=' + asm_code;

    fetch(url)
        .then(response => response.json())
        .then(data => display_translation(data))
        .catch(error => console.log(error));
}

const display_translation = (c_output) => {
    // c_output is translated asm code as one string
    document.getElementById('loader').classList.add('hidden');
    document.getElementById('c-output').value = c_output;
    // can style or print token by token, but for now, just write all
    // let x = 0;
    // for (token of c_output.split(' ')) {   
    //     setTimeout(() => {document.getElementById('c-output').value += token + ' '}, x);
    //     x += 500;
    // }
    
    document.getElementById('c-output').setAttribute('placeholder', 'int f() {\n\treturn 0;\n}');
}