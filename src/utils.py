#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:30:24 2018

@author: nicholas
"""
import logging
import argparse
from torch import save
import time
from os import path as path

def parse_arg():
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(asctime)s]: %(levelname)s: %(message)s"
    )
    parser = argparse.ArgumentParser(description='train.py')
    parser.add_argument('-pretrained_model_path', type=str, default='./model.t7')
    parser.add_argument('-batch_size', type=int, default=1)
    parser.add_argument('-train_file_path', type=str, default='./train.txt')    
    parser.add_argument('-eval_file_path', type=str, default='./eval.txt')
    parser.add_argument('-num_output', type=int, default=3)
    parser.add_argument('-model_type', type=str, default='VGG16')
    parser.add_argument('-lr', type=float, default=0.01, help="sgd: 10, adam: 0.001")
    parser.add_argument('-gpuid', type=int, default=0)
    parser.add_argument('-epochs', type=int, default=10)
    parser.add_argument('-report_every', type=int, default=10)
    # whether to apply data augmentation
    parser.add_argument('-transform', type=bool, default=False)
    # whether to perform evaluation on evaluation set during training
    parser.add_argument('-eval', type=bool, default=True)
    parser.add_argument('-eval_every', type=int, default=500)
    parser.add_argument('-save_dir', type=str, default='../model')
    parser.add_argument('-save_name', type=str, default='fine_tuned_model')
    opt = parser.parse_args()
    return opt

def get_save_dir(opt):
    save_name = path.join(opt.save_dir, opt.save_name)
    save_name += 'model_type'
    save_name += opt.model_type
    save_name += '.t7'
    save_name += time.asctime(time.localtime(time.time()))
    return save_name

def save_model(model, opt):
    # helper function for saving a trained model
    save_name = get_save_dir(opt)
    save(model, save_name)