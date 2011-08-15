# search for rst2s5(.py)

  rst2s5 := $(shell which rst2s5)
  rst2s5 := $(if $(rst2s5), $(rst2s5), $(shell which rst2s5.py))

slides slides.html: gitegg.rst
	$(rst2s5) gitegg.rst slides.html
