# To detect gender according to name
# to run this use pip install gender-guesser
name="Bob" # name for which gender to be decided
import gender_guesser.detector as gender
d = gender.Detector()
a=d.get_gender(name)
print(a)
