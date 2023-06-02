// Asagidaki 1'den 30'a kadar 15-20 arasindaki sayilari[15-20] atlayarak yazdiran kodda hata almamizin sebabi nedir? declare @sayac5 int=0 while @sayac5 <30 begin print @sayac5 if @sayac5 between 15 and 20 continue set @sayac5+=1 end;
// a) • Sonsuz döngüye girdigi için hata vardir.
// b) O continue yerine break yazilmadigi için hata verir.
// c) • Degisken tanimlamada hata vardir.
// d) O Kodda hata yoktur.
// e) • Kodda syntax hatasi vardir.

// answer 