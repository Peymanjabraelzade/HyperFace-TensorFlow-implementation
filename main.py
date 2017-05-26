import tensorflow as tf
import os
from model import *


weights_path = '/Users/shashank/Tensorflow/SPN/weights/'
imgs_path = '/Users/shashank/Tensorflow/CSE252C-Hyperface/git/truth_data.npy'

if not os.path.exists('./logs'):
	os.makedirs('./logs')

map(os.unlink, (os.path.join( './logs',f) for f in os.listdir('./logs')) )

net = HyperFace(tf_record_file_path='../../aflw_train_small_new.tfrecords')

with tf.Session() as sess:
		print 'Building Graph...'
		net.build_network(sess,False,model_save_path='../../checkpoint',best_model_save_path='../../best_checkpoint')
		print 'Graph Built!'
		# net.print_variables()
		# net.load_weights(weights_path)
		net.train()

