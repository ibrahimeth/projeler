def hesapoyun()
    print "0 dan kaça kadar tahmin etmek istersiniz :"
    m = gets.chomp.to_i
    x = rand(m)
    hak = m*3/10.round
    puan = 100
    sayaç = hak
    puan_düsürücü = 100/hak
    print "TANIMLANAN HAK : #{hak} \n "
    loop do
        puan = puan - puan_düsürücü
        print "bir sayı tahmin ediniz 0 ile #{m} arasında :"
        value = gets.chomp.to_i
        hak -= 1
        if value == x 
            puts "TEBRİKLER , bildiniz PUAN DURUMU : #{puan} "
            break
        elsif  hak == 0
            puts "maalesef hakkınız bitti , bir sonraki sefere :D"
            break
        end        
    end
end
hesapoyun