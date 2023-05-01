import os
import tensorflow as tf
import time

from transformer.decoder import Decoder
from transformer.encoder import Encoder
from transformer.util import CustomSchedule, masked_loss, masked_accuracy
from transformer.dataprocess import Translator, DataLoader, \
    partition_into_batches


RANDOM_SEED = 42069


class NeuralDecompiler(tf.keras.Model):
    '''
    Implementation help from the tutorial: 
    https://www.tensorflow.org/text/tutorials/transformer
    '''

    def __init__(self, emb_sz, input_vocab_size, output_vocab_size, 
                 ff_hidden_dim, num_layers, num_heads, dropout=0.0):
        
        super().__init__()

        self.encoder = Encoder(
            emb_sz=emb_sz,
            vocab_sz=input_vocab_size,
            ff_hidden_dim=ff_hidden_dim,
            num_layers=num_layers,
            num_heads=num_heads,
            dropout=dropout
        )

        self.decoder = Decoder(
            emb_sz=emb_sz,
            vocab_sz=output_vocab_size,
            ff_hidden_dim=ff_hidden_dim,
            num_layers=num_layers,
            num_heads=num_heads,
            dropout=dropout
        )

        self.linear = tf.keras.layers.Dense(output_vocab_size)

    def call(self, inputs):
        """
        @params
        - inputs: a tuple (context, target), where context is the input ASM 
            code, and target is the input C code
        """

        context, target = inputs
        context = self.encoder(context)
        logits = self.decoder(target, context)

        logits = self.linear(logits)

        # from the TensorFlow Transformer tutorial 
        try:
            del logits._keras_mask
        except AttributeError:
            pass

        return logits





def train(num_epochs, batch_size):

    #### Load data
    current_dir = os.path.dirname(os.path.realpath(__file__))


    # c_dir = "../data/leetcode_renamed_data/C_COMPILED_FILES"
    # asm_dir = "../data/leetcode_renamed_data/ASM_COMPILED_FILES"
    c_dir = "tiny_dataset/C"
    asm_dir = "tiny_dataset/ASM"


    c_path = f"{current_dir}/{c_dir}"
    asm_path = f"{current_dir}/{asm_dir}"

    loader = DataLoader(c_path=c_path, asm_path=asm_path)
    c_vals, asm_vals, stats = loader.load_data()

    c_vocab_size = stats['max_asm_code_length']
    asm_vocab_size = stats['max_asm_code_length']
    #### End loading data


    ## TUNE HYPERPARAMS
    emb_sz = 128

    model = NeuralDecompiler(emb_sz=emb_sz, 
                             input_vocab_size=asm_vocab_size,
                             output_vocab_size=c_vocab_size,
                             ff_hidden_dim=128,
                             num_layers=6,
                             num_heads=8,
                             dropout=0.05)
    
    lr = CustomSchedule(d_model=emb_sz)
    optimizer = tf.optimizers.Adam(lr, 
                                   beta_1=0.9,
                                   beta_2=0.98, 
                                   epsilon=1e-9)
    ## TUNE HYPERPARAMS


    # Set up checkpoint
    checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)


    # FOR ALL EPOCHS
    for epoch in range(num_epochs):

        tic = time.perf_counter()

        c_batches, asm_batches = partition_into_batches(c_vals, asm_vals, 
                                                        batch_size)
        
        batch_loss = 0
        batch_acc = 0

        # TRAIN STEP
        for c_batch, asm_batch in zip(c_batches, asm_batches):

            decoder_input = c_batch[:, :-1]
            decoder_labels = c_batch[:, 1:]

            with tf.GradientTape() as tape:
                pred = model((asm_batch, decoder_input))
                loss = masked_loss(decoder_labels, pred)
                acc = masked_accuracy(decoder_labels, pred)
            
            batch_loss += loss
            batch_acc += acc

            gradients = tape.gradient(loss, model.trainable_weights)
            optimizer.apply_gradients(zip(gradients, model.trainable_weights))

        batch_loss /= batch_size
        batch_acc /= batch_size

        toc = time.perf_counter()

        print(f"epoch: {epoch} | loss: {batch_loss} | acc: {batch_acc}" + \
              f" time elapsed: {toc-tic}", end="\n")
    
    print("training complete . . .")
    checkpoint_path = "/../model_checkpoints/model-checkpoint"
    print(f"saving model checkpoint to {checkpoint_path}")
    checkpoint.save(checkpoint_path)

if __name__ == "__main__":
    train(10, 4)

