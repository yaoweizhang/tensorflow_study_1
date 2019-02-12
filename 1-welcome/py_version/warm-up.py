import os
import tensorflow as tf

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
tf.app.flags.DEFINE_string("log_dir", log_dir,
        "Directory where event logs are written to.")

FLAGS = tf.app.flags.FLAGS

welcome = tf.constant("welcome to tensorflow world!")

with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("output: ", sess.run(welcome))

writer.close()
sess.close()
