https://replit.com/join/dpptoaxxih-emilianogarci39

#the care for ruby the plant

temperature = input("please enter the temperature: ")
humidity = input("please enter the humidity: ")
day = input("please enter the day: ")



if int(temperature) <20: 
  print("you should bring ruby inside the house")

elif int(temperature) > 25:
  print("bring ruby inside turn on the fan")

else:
  
  print("good conditions for ruby")  

if day in ["Tuesday","Thursday","saturday"]:
     print("water ruby.")

elif int(humidity) <20:
    print("you should water it")

elif 20<=  int(humidity) <= 22:
    print("suitable humidity for ruby")

elif  int(humidity) > 22 and day in ["monday","wednesday","friday","sunday"]:
          print("it is not necesary to water ruby") 

else:
  print("no specific care required today")


