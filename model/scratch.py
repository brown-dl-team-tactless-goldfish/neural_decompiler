import numpy as np
import tensorflow as tf


# window_size_queries = 10
# window_size_keys = 5


# mask_vals = np.logical_not(np.triu(np.ones((window_size_queries, window_size_keys)), k=1))
# mask = tf.convert_to_tensor(value=mask_vals, dtype=tf.bool)

# print(mask)



# # print(mask)

# # atten_mask = tf.tile(tf.reshape(mask, [-1, window_size_queries, 
# #                                 window_size_keys]), 
# #                             [window_size_keys, 1, 1])

# # print(atten_mask)


# mask_vals = np.triu(np.ones((window_size_queries, window_size_keys)) * \
#                             np.NINF, k=1)
# mask = tf.convert_to_tensor(value=mask_vals, dtype=tf.float32)
# print(mask)


# from transformer.encoder import Encoder


print(tf.random.shuffle(tf.range(10)))