#!/usr/bin/python

import tensorflow as tf

print("hello")
a=tf.constant(1)
b=tf.constant(2)

sum=tf.add(a,b)

sess=tf.Session()

print(sess.run(sum))
