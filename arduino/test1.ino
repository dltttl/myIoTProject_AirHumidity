int humidity = 0;

void setup()
{
	Serial.begin(9600);
}

void loop()
{
  humidity = analogRead(A0);
  humidity = map(humidity, 0, 1023, 0, 100);
	Serial.println(humidity);
	delay(100);
}
