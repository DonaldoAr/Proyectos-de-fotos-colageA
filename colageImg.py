import os
import cv2
import numpy as np
import time
# 768*512
# * HACER UNA FUNCION, PEDIR #IMAGENES, CARPETAS DE IAMGENES, IMAGEN_AGUA -> RETORNA IMAGEN 
# final1 = np.zeros((1080, 1920), dtype=np.uint8)
def opacidadImagenes(PathImgOri ,PathImagenesRe, PathImagenAgua, con):
    """
        PathImgOri: Imagenes originales donde se guardan,
        PathImagenesRe: Carpeta de las imagenes recortadas,
        PathImagenAgua: Ruta completa de la imagen que se guarda, la img debe tener resolución de 1920x1080,
        con: Numero de imagenes que se han tomando fotos
    """
    # DETERMINAR EL MUERO DE FOTOS EN LA CARPETA
    # path, dirs, files = next(os.walk(r"./public/Img"))    
    # path, dirs, files = next(os.walk(PathImagenesRe))    
    # file_count = len(files)
    time.sleep(0.5)
    # print(file_count)
    img2 = cv2.imread(PathImagenAgua)
    size_imgMo = np.shape(img2)  # (90, 160, 3)
    # final = np.zeros((1080, 1920, 3), dtype=np.uint8)
    # 768*512
    final = np.zeros((512, 768, 3), dtype=np.uint8)
# CONDICIONALES DE #NUMERO DE IMAGENES QUE HAY EN LA CARPETA   
    if con == 1:
        # CAMBIAR EL TAMAÑO DE LA PRIMERA IMAGEN A 1920X1080
        resize(1, PathImgOri, PathImagenesRe, 768, 512)
        img1 = cv2.imread(PathImagenesRe+"/1.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite("fin1.jpg",total)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        
        # cv2.imshow('', total)
        # cv2.waitKey(0)
    # CUANDO HAY 2 IMG
    elif con == 2:
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1,3):
            resize(imagen, pathImagenes, pathRecortes, 384, 512)
        # COLLAGE
        im = 1
        for col in range(2):
            # print(reg,col)
            little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
            concat_h1 = cv2.hconcat([little])
            final[0 * 90: (1) * 512, col * 384: (col+ 1) * 384] = concat_h1
            im += 1
            if im == 8:
                im = 1
        concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite("fin2.jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
    # CUANDO HAY 3 IMG
    elif con == 3:
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 256, 512)
        # COLLAGE
        im = 1
        for col in range(3):
            # print(reg,col)
            little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
            concat_h1 = cv2.hconcat([little])
            final[0 * 512: (1) * 512, col * 256: (col+ 1) * 256] = concat_h1
            im += 1
            if im == 8:
                im = 1
        concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite("fin3.jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
    # CUANDO HAY 4 IMAGENES
    elif con == 4:
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 384, 256)
        im = 1
        for reg in range(2):
            for col in range(2):
                # print(reg,col)
                little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
                concat_h1 = cv2.hconcat([little])
                final[reg * 256: (reg + 1) * 256, col * 384: (col+ 1) * 384] = concat_h1
                im += 1
                if im == (con+1):
                    im = 1
            concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite("fin4.jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
    # CUANDO HAY 5 a 6 IMAGENES
    elif(con <= 6 and con > 4):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 256, 256)
        im = 1
        for reg in range(2):
            for col in range(3):
                # print(reg,col)
                little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
                concat_h1 = cv2.hconcat([little])
                final[reg * 256: (reg + 1) * 256, col * 256: (col+ 1) * 256] = concat_h1
                im += 1
                if im == (con+1):
                    im = 1
            concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
    # CUANDO HAY 6 IMAGENES           
    elif(con < 9 and con > 6):
         # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 192, 256)
        im = 1
        for reg in range(2):
            for col in range(4):
                # print(reg,col)
                little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
                concat_h1 = cv2.hconcat([little])
                final[reg * 256: (reg + 1) * 256, col * 192: (col+ 1) * 192] = concat_h1
                im += 1
                if im == (con+1):
                    im = 1
            concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)            
        cv2.imwrite("./static/downloads/fin.jpg",total)
    # CUANDO HAY 9 IMAGENES     
    elif con == 9:
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 256, 170)
        im = 1
        for reg in range(3):
            for col in range(3):
                # print(reg,col)
                little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
                concat_h1 = cv2.hconcat([little])
                final[reg * 170: (reg + 1) * 170, col * 256: (col+ 1) * 256] = concat_h1
                im += 1
                if im == (con+1):
                    im = 1
            concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)                     
    elif (con <= 12 and con > 9):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 192, 170)
        im = 1
        for reg in range(3):
            for col in range(4):
                # print(reg,col)
                little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
                concat_h1 = cv2.hconcat([little])
                final[reg * 170: (reg + 1) * 170, col * 192: (col+ 1) * 192] = concat_h1
                im += 1
                if im == (con+1):
                    im = 1
            concat_v = cv2.vconcat([concat_h1])
        cv2.imwrite("tlaxcalaFin.jpg",final)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite("fin11.jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)                   
    elif(con <= 16 and con > 12):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 192, 128)

        concantenar(PathImagenesRe, 4, 4, 192, 128, final, con = con)

        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)      
    elif(con <= 25 and con > 16):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 153, 102)
        concantenar(PathImagenesRe, 5, 5, 153, 102, final, con = con)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0) 
    elif(con <= 36 and con > 25):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        # print("6")
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 128, 85)
        concantenar(PathImagenesRe, 6, 6, 128, 85, final, con = con)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
    elif(con <= 64 and con > 36):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        # print("8")
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 96, 64)
        concantenar(PathImagenesRe, 8, 8, 96, 64, final, con = con)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
    elif(con <= 100 and con > 65):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        # print("10")
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 76, 51)
        concantenar(PathImagenesRe, 10, 10, 76, 51, final, con = con)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        # total = cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=0.5, gamma=0)
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)
    elif(con <= 5041 and con > 100):
        # CAMBIAR EL TAMAÑO DE LA IMAGENES
        # print("10")
        pathImagenes = PathImgOri
        pathRecortes = PathImagenesRe
        for imagen in range(1, con + 1):
            resize(imagen, pathImagenes, pathRecortes, 10, 7)
        concantenar(PathImagenesRe, 71, 71, 10, 7, final, con = con)
        img1 = cv2.imread("tlaxcalaFin.jpg")
        # total = cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=0.5, gamma=0)
        total = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.6, gamma=0)
        cv2.imwrite("./static/downloads/fin.jpg",total)
        # cv2.imwrite(r"fin"+str(con)+r".jpg",total)
        # cv2.imshow('', total)
        # cv2.waitKey(0)          
              

# FUNCION PARA REDIMENSIONAR LAS IMAGENES
def resize(imagen, pathImagenes, pathRecortes, ancho, alto):
    """
        pathImagenes: Direccion de las imagene donde llegan y se guardan,
        pathRecortes:  Direccion donde se guardan las iamgenes a recortar
    """
    imgPath = pathImagenes + r"/" + str(imagen) + ".jpg" # Construir ruta de la imagen
    img = cv2.imread(imgPath)              # Leer la imagen a la memoria img variable
    image = cv2.resize(img, (ancho, alto))      # 28, 28
    # == Imagen donde  se guarda
    cv2.imwrite(pathRecortes + r"/" + str(imagen) + ".jpg",image)
    pass

def concantenar(PathImagenesRe, R, C, ancho, alto, final, con):
    im = 1
    for reg in range(R):
        for col in range(C):
            little = cv2.imread(PathImagenesRe+r"/"+str(im)+".jpg")
            concat_h1 = cv2.hconcat([little])
            # final[reg * alto: (reg + 1) * alto, col * ancho: (col+ 1) * ancho] = concat_h1
            final[reg * alto: (reg + 1) * alto, col * ancho: (col+ 1) * ancho] = concat_h1
            im += 1
            if im == (con+1):
                im = 1
        concat_v = cv2.vconcat([concat_h1])
    cv2.imwrite("tlaxcalaFin.jpg",final)