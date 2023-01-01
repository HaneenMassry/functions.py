import moviepy.editor as mp
from pydub import AudioSegment
import math
import os

import speech_recognition as sr
from os import path
from pydub import AudioSegment

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, storage

from json import JSONEncoder





def uploadfinal():

  def extractAud(vid):
      my_clip = mp.VideoFileClip(vid)
      # my_clip
      audio_clip = my_clip.audio
      audio_clip.write_audiofile(r"my_result.mp3")


  # קובץ תמלול עם זמנים
  def subtitelsSRT(my_result):
      class SplitWavAudioMubin():
          def __init__(self, folder, filename):
              self.folder = folder
              self.filename = filename
              self.filepath = folder + '\\' + filename

              self.audio = AudioSegment.from_wav(self.filepath)

          def get_duration(self):
              return self.audio.duration_seconds

          def single_split(self, from_min, to_min, split_filename):
              t1 = from_min * 60 * 1000
              t2 = to_min * 60 * 1000
              split_audio = self.audio[t1:t2]
              split_audio.export(self.folder + '\\' + split_filename, format="wav")

          def multiple_split(self, min_per_split):
              total_mins = math.ceil(self.get_duration() / 60)
              for i in range(0, total_mins, min_per_split):
                  split_fn = str(i) + '_' + self.filename
                  self.single_split(i, i + min_per_split, split_fn)
                  print(str(i) + ' Done')
                  if i == total_mins - min_per_split:
                      print('All splited successfully')
              return total_mins

      import datetime
      block_num = "16"

      def time_addition(sentence, current_time):
          time_add = (len(sentence.split())) * .5
          end_time = current_time + datetime.timedelta(0, time_add)
          str_current_time = str(current_time.time())
          str_end_time = str(end_time.time())

          with open(Srt_File, "a") as f:
              f.write(block_num)
              f.write("\n")
              f.write(str_current_time)
              f.write("-->")
              f.write(str_end_time)
              f.write("\n")
              f.write(sentence)
              f.write("\n")
              f.write("\n")
          return end_time

      start_time = datetime.datetime(100, 1, 1, 0, 0, 0)

      # Press the green button in the gutter to run the script.
      if __name__ == '__main__':

          # convert mp3 file to wav
          sound = AudioSegment.from_mp3("my_result.mp3")
          sound.export("transcript.wav", format="wav")

          # transcribe audio file
          AUDIO_FILE = "transcript.wav"

          split_wav = SplitWavAudioMubin(os.getcwd(), AUDIO_FILE)
          num_of_files = split_wav.multiple_split(1)
          print("num of files " + str(num_of_files))

          # iterate through all files and each add to srt file

          for i in range(0, num_of_files):
              file_part = str(i) + "_" + AUDIO_FILE #todo hiiiii
              # use the audio file as the audio source
              r = sr.Recognizer()
              with sr.AudioFile(file_part) as source:
                  audio = r.record(source)  # read the entire audio file
                  sentence = r.recognize_google(audio)

                  print("Transcription: " + sentence)
                  start_time = time_addition(sentence, start_time)


  # عمل كائن باسم حصة
  def creatLesson(Subject, Teacher, Class, Video, Srt_File,vidLink,srtLink):
      class Lesson:
          # Class Variable
          lesson = 'LClass'

          # The init method or constructor
          def __init__(self, Subject, Teacher, Class, Video, Srt_File,vidLink,srtLink):
              # Instance Variable
              # schoolname
              self.Subject = Subject
              self.Teacher = Teacher
              self.Class = Class
              self.Video = Video
              self.Srt_File = Srt_File
              self.vidLink = vidLink
              self.srtLink = srtLink

          # Retrieves instance variable
          def getSubject(self):
              return self.Subject

          def getTeacher(self):
              return self.Teacher

          def getClass(self):
              return self.Class

          def getVideo(self):
              return self.Video

          def getSrtFile(self):
              return self.Srt_File


  # העלאת קבצים לפיירביס
  def uploadLesson():
      # 2 options -> same name' just differnt ending
      # other options - 2 different directot=ries one for mp4 other for txt file
      filename = Video
      filename1 = Srt_File

      cred = credentials.Certificate('firebase-sdk.json')
      firebase_admin.initialize_app(cred, {

          'storageBucket': 'uploadtest-2e678.appspot.com',

          'databaseURL': 'https://uploadtest-2e678-default-rtdb.firebaseio.com/'
      })

      bucket = storage.bucket()
      blob = bucket.blob("Schools/"+School + Subject+"/" + Teacher + "/" + Class + "/" + "Video_Files/" + filename)
      blob.upload_from_filename(filename)

      blob = bucket.blob("Schools/"+School + Subject+"/" + Teacher + "/" + Class + "/" + "TXT_Files/" + filename1)
      blob.upload_from_filename(filename1)

  # database:
  # school:
  #       name:"school a"
  #        classes "10,11,12"
  #        Teachers "allon,sameh,...."
  #        Subjects "Math,computer Science"

  # student
  #       school
  #       class
  #       teachers
  #       subjects

  # Teacher
  #       school name
  #       teacherName
  #       subjects "Math,CS..."
  #       class "10,11,12"

  # check if there is a package that called acording of what we want>> if not creat one >> if true print "TRUE"

  # input the subject name&date
  Class = (str)(input("write which class"))
  Subject = (str)(input("write the subject name"))
  Teacher = (str)(input("teacher name"))
  School = (str)(input("SChool name "))
  lessonName = (str)(input("Write lesson name"))
  Video=lessonName+".mp4"
  Srt_File = lessonName+".txt"

  extractAud(Video)
  subtitelsSRT('my_result.mp3')
  uploadLesson()

