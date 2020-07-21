import tensorflow.compat.v1 as tf

hello = tf.constant("Hello, tensorflow")

sess = tf.Session()

print(sess.run(hello))