name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightCM = round(height * 2.5)
weight = 180 # lbs
weightKG = round(weight * 0.454)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %.2f centimeters tall." % heightCM
print "He's %.2f kilograms heavy." % weightKG
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %r, and %r I get %d." % (
    age, heightCM, weightKG, age + heightCM + weightKG)
