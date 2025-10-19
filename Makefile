TARGET=gberweb

init:
	mvn use v22

build:
	npm run build

deploy:
	$(MAKE) build
	cp -rfv dist/* $(TARGET)
	git log -n 2 > $(TARGET)/version.txt
	git -C $(TARGET) add .
	git -C $(TARGET) commit -a -m "Auto deploy `date --iso-8601`"
	git -C $(TARGET) push --force origin master

