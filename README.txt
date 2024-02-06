https://github.com/anishathalye/imagenet-simple-labels

#running dcokerize
docker build -t x4 .

#starting container
docker container run -d -p 5000:5000 x4

Prosta aplikacja wykorzystujaca model tensorflow w celu rozpoznawania obiektów na zdjęciu. Korzysta z api - Flask
Aplikacja przygotowana do dokeryzacji.
