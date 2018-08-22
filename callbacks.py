import csv
import os

from keras.callbacks import Callback


class LogAfterBatch(Callback):
    def __init__(self, filename='run_log_keras.csv'):
        self.filename = filename
        self.step = 0
        self.val_acc = None
        self.val_loss = None

    def on_train_begin(self, logs=None):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def on_batch_end(self, batch, logs={}):
        self.step += 1
        loss = logs.get('loss')
        acc = logs.get('acc')

        if self.val_acc is None:
            self.val_acc = acc
        if self.val_loss is None:
            self.val_loss = loss

        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([
                batch,
                acc,
                loss,
                self.val_acc,
                self.val_loss
            ])

    def on_epoch_end(self, epoch, logs={}):
        val_acc = logs.get('val_acc')
        val_loss = logs.get('val_loss')

        self.val_acc = val_acc
        self.val_loss = val_loss
