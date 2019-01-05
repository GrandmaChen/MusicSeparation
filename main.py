import tensorflow as tf

hello = tf.constant('Nah Im just testing')

sess = tf.Session()

print(sess.run(hello))
