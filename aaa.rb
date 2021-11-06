def hesapoyun()
    x = rand(10)
    loop do
        print "bir sayı tahmin ediniz 1 ile 10 arasında "
        value = gets.chomp
        if value == x 
            puts "bildiniz"
            break
        else
            value
        end        
    end
end

hesapoyun