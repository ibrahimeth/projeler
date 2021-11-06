def hesapoyun()
    print "0 dan kaça kadar tahmin etmek istersiniz :"
    m = gets.chomp.to_i
    x = rand(m)
    hak = m*3/10.round
    sayaç = 0
    puan_düsürücü = 100/hak
    print "TANIMLANAN HAK : #{hak} \n "
    loop do
        sayaç += 1
        puan = 100 - puan_düsürücü * (sayaç -1)
        print "bir sayı tahmin ediniz 0 ile #{m} arasında :"
        value = gets.chomp.to_i
        hak -= 1
        if value == x 
            puts "TEBRİKLER , bildiniz PUAN DURUMU : #{puan} "
            break
        elsif  hak == 0
            puts "maalesef hakkınız bitti , bir sonraki sefere :D"
            break
        elsif value < x
            puts "YUKARI"
        elsif value > x
            puts "AŞAĞI"
        end        
    end
end
hesapoyun