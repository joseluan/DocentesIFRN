import urllib.request

site = 'http://docente.ifrn.edu.br/'
arquivo = open("_nomes.txt",'r')

for docente in arquivo.readlines():
    docente = docente.replace("\n","")
    url = site  + docente +"/image_preview"
    print(url)
    try:
        foto = urllib.request.urlopen(url).read()
        file = open(docente+".jpg",'wb')
        file.write(foto)
        file.close()
    except:
        print ("erro...")
