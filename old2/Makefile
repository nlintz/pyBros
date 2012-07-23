html=run.html
mvp=mvp.js
jit=Jit/
bootstrap=bootstrap/
images=pybros.gif pybros.png
all=$(html) $(mvp) $(jit) $(bootstrap)

web: $(all)
	cp -r $(all) /var/www

clean:
	rm -rf /var/www/*
