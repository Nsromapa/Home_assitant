import pickle

from classifier_cleaner import input_process

ans = input_process('how will the weather be today')

classifier = pickle.load(open('classifier_model.sav', 'rb'))
results = classifier.predict(ans)

print(results)

if results == 'weather':
  print('go ahead')