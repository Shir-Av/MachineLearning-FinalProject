import fnmatch
import os

from pydub import AudioSegment
from pydub.utils import make_chunks


def cut_to_chunks(path, label):
    for root, dirnames, filenames in os.walk(path):
        for i, filename in enumerate(fnmatch.filter(filenames, '*.wav')):
            print(filename)
            my_audio = AudioSegment.from_file(os.path.join(root, filename), "wav")
            chunk_length_ms = 1000  # pydub calculates in millisec
            chunks = make_chunks(my_audio, chunk_length_ms)  # Make chunks of one sec

            # Export all of the individual chunks as wav files

            for j, chunk in enumerate(chunks):
                chunk_name = f'{path}/{label}_chunk{i}-{j}.wav'.format(i)
                print("exporting", chunk_name)
                chunk.export(chunk_name, format="wav")


def cut_a_single_record(path):
    record_file = path + '.wav'
    record_label = path + '.txt'
    my_audio = AudioSegment.from_file(record_file, "wav")
    chunk_length_ms = 1000  # pydub calculates in millisec
    chunks = make_chunks(my_audio, chunk_length_ms)  # Make chunks of one sec

    with open(record_label, 'r') as file_handle:
        labels = []
        for line in file_handle:
            labels.append(line.strip())

    chunks_list = []
    for i, chunk in enumerate(chunks):
        chunk_name = f'./clf_classes/_chunk{i}.wav'.format(i)
        print("cut", chunk_name)
        chunk.export(chunk_name, format="wav")
        chunks_list.append(chunk_name)

    return [chunks_list, labels]