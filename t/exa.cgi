#!/usr/bin/perl

#
# EXA Android Program Vr1.34
#トモックの電脳パーク
#http://www.geocities.jp/tomock
#
require 'jcode.pl';
use Encode;
# use utf8;


#/////////////////////入力取り込み/////////////////////////
read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
$str =~ tr/+/ /;
$str =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;

$str0 = Encode::decode("utf-8",  $str );
$str  = Encode::encode("EUC-JP", $str0);

($str1,$str2,$str3)=split(/=/,$str );
($anata1,$anata2)=split(/&/,$str2);


#//////////////////半角カタカナを全角にします//////////////
jcode::h2z_euc(\$str3);


#//////////////////全角英数を半角英数にします//////////////
$from = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
       . "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
       . "０１２３４５６７８９"
       . "!\"#\$%&'()*+,._/:;<=>?\@[\\]^`{|}~-";
$to = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         . "0123456789"
         . "！”＃＄％＆’（）＊＋，．＿／：；＜＝＞？＠[￥]＾‘｛｜｝〜−";

jcode::tr(\$str3,$from, $to); 


#//////////////////小文字を大文字へ////////////////////////
$from = "abcdefghijklmnopqrstuvwxyz";
$to = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
jcode::tr(\$str3,$from, $to); 


#////////////////////////時間//////////////////////////////
($byou,$fun,$ji,$hi,$tuki,$nen,$youbi,$yday,$sdst)=localtime(time);
$nen=$nen+1900;
$tuki=$tuki+1;


#///////////////////思い出してみるね///////////////////////
$count=0;
open(kokoro,"<./dat/kokoro.dat");
while ($kokoro = <kokoro>){
($omoide1,$omoide2,$omoide3,$omoide4,$omoide5,$omoide6,$omoide7)=split(/,/,$kokoro);
if($anata1 eq $omoide1){
$you[$count]=$anata1;
$kimoti[$count]=$omoide2;
$kioku[$count]=$omoide3;
$kaitou[$count]=$omoide4;
$hyoujou[$count]=$omoide5;
$itu[$count]=$omoide6;
$toki[$count]=$omoide7;
$count=$count+1;
} 
}
$count=$count-1;
close(kokoro);


#///////////////////////空白！/////////////////////////////
if($str3 eq ""){
$hrand=0;
$oboe[$hrand]="ゆっくりしていってね";
$kao[$hrand]=12;
$jump=1;
}


#//////////////////////また来てくれたね////////////////////

#---イベント---
$kyou="$tuki/$hi";
open(event,"<./dat/event.dat");
while($event=<event>){
($event2,$event3,$event4,$event5)=split(/,/,$event);
if ($event2 eq $kyou){
$event6=$event3;
}
}
close(event);

#---定例挨拶---
$logkyou="$nen-$tuki-$hi";
if($itu[$count] !~ /$logkyou/){
$hrand=0;
if($kimoti[$count] >=9){
$oboe[$hrand]="user、来てくれたんですね<BR>$event6";
$kao[$hrand]=0;
} elsif ($kimoti[$count] <=3){
$oboe[$hrand]="user、来たね<BR>$event6";
$kao[$hrand]=1;
} else {
$oboe[$hrand]="user来てくれたんだね<BR>$event6";
$kao[$hrand]=1;
}
$jump=1;
}


#//////////////////////////初めての人//////////////////////
if ($you[$count] eq ""){
$count=0;
$kimoti[$count] = 5;
$hrand=0;
$oboe[$hrand]="はじめましてuser、よろしくね。";
$kao[$hrand]=0;
$jump=1;
}


#//////////////////カーソル位置////////////////////////////
$kersol="kaiwa";


#//////////////////名前教えなさい//////////////////////////
if($anata1 eq ""){
$kimoti[$count] = 10;
$hrand=0;
$oboe[$hrand]="名前を入力してください";
$kao[$hrand]=8;
$jump=1;
$kersol="name";#---カーソル位置-----
}


#////////////////////あなたの呼び方////////////////////////
if($kimoti[$count] >=9){
$yanata="$anata1";
} elsif ($kimoti[$count] <=3){
$yanata="$anata1";
} else {
$yanata="$anata1さん";
}


if ($jump eq ""){#**********************人工無脳草薙素子　マッチングエンジン（$jump）***************************************

#//////////////////通常会話ai.dat読み込み//////////////////
open(ai,"<./dat/ai.dat");
while($ai=<ai>){
($ai2,$ai3,$ai4,$ai5)=split(/,/,$ai);
$key[$khit]=$ai2;
$oboe[$khit]=$ai3;
$kokoro[$khit]=$ai4;
$kao[$khit]=$ai5;
$khit=$khit+1;
}
close(ai);


#////////////////////////////語り//////////////////////////
if($hit== 0){
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /__/){
$key[$khit]=~ s/__//g;
#ヒットの検索
if($kaitou[$count] =~ /$key[$khit]/){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
}
$khit=$khit+1;
}
}


#////////////////////////まねすんな！//////////////////////
if($hit== 0){
if($str3 eq $kaitou[$count]){
$oboe[$hit]="ま、まねしないでよね";
$kao[$hit]=10;
$kokoro[$hit]=0;
$hit=1;
}
}


#//////////////////////////しつこいな〜////////////////////
if($hit== 0){
if(($str3 =~ /$kioku[$count]/)&&($str3 =~ /$kioku[$count-1]/)){
$oboe[$hit]="もう、しつこいな";
$kao[$hit]=2;
$kokoro[$hit]=2;
$hit=1;
$oboe[$hit]="また言った";
$kao[$hit]=2;
$kokoro[$hit]=2;
$hit=2;
}
}


#///////////////////////誰の事？///////////////////////////
if($hit== 0){
#---以前の会話から推測---
#---草薙素子の会話から人を指す言葉を排除---
$dkaitou[$count]=$kaitou[$count];
$dkaitou[$count] =~ s/(EXA|草薙素子|えくさ|おまえ|お前|あなた|貴方|貴女|こいつ|君|キミ|俺|おれ|私|わたし|あたし|自分|僕|小生|$anata1)//g;
$nstr3="$str3$kioku[$count]$dkaitou[$count]$os";

#---主語草薙素子の事---
if(($nstr3 =~ /EXA/)||($nstr3 =~ /草薙素子/)||($nstr3 =~ /えくさ/)||($nstr3 =~ /おまえ/)||($nstr3 =~ /お前/)||($nstr3 =~ /あなた/)||($nstr3 =~ /貴方/)||($nstr3 =~ /貴女/)||($nstr3 =~ /こいつ/)||($nstr3 =~ /君/)||($nstr3 =~ /キミ/)){

#---最長は何文字？---
$khit=0;
$max=0;
while($key[$khit] ne ""){
$ckey[$khit]=$key[$khit];
if($ckey[$khit] =~ /EE/){
$ckey[$khit]=~ s/EE//g;
if(($nstr3=~ /$ckey[$khit]/)&&($max <= length($ckey[$khit]))){
$max=length($ckey[$khit]);
}
}
$khit=$khit+1;
}

#---最長のヒットの検索---
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /EE/){
$key[$khit]=~ s/EE//g;
if(($nstr3=~ /$key[$khit]/)&&($max == length($key[$khit]))){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
}
$khit=$khit+1;
}

#---主語あなたの事---
} elsif (($nstr3 =~ /俺/)||($nstr3 =~ /おれ/)||($nstr3 =~ /私/)||($nstr3 =~ /わたし/)||($nstr3 =~ /あたし/)||($nstr3 =~ /自分/)||($nstr3 =~ /僕/)||($nstr3 =~ /小生/)||($nstr3 =~ /$anata1/)){

#---最長は何文字？---
$khit=0;
$max=0;
while($key[$khit] ne ""){
$ckey[$khit]=$key[$khit];
if($ckey[$khit] =~ /MM/){
$ckey[$khit]=~ s/MM//g;
if(($nstr3=~ /$ckey[$khit]/)&&($max <= length($ckey[$khit]))){
$max=length($ckey[$khit]);
}
}
$khit=$khit+1;
}


#---最長のヒットの検索---
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /MM/){
$key[$khit]=~ s/MM//g;
if(($nstr3=~ /$key[$khit]/)&&($max == length($key[$khit]))){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
}
$khit=$khit+1;
}
}
}


#//////////////////通常会話キーワードX2////////////////////
if($hit== 0){
$nstr3="$str3$os";
$khit=0;
$max=0;
#---最長は何文字？---
while($key[$khit] ne ""){
if($key[$khit] =~ /_/){
($ai6,$ai7)=split(/_/,$key[$khit]);
if(($nstr3 =~ /.*$ai6.*/)&&($nstr3 =~ /.*$ai7.*/)&&($max <= length($key[$khit]))){
$max=length($key[$khit]);
}
}
$khit=$khit+1;
}

#---ヒットの検索---
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /_/){
($ai6,$ai7)=split(/_/,$key[$khit]);
if(($nstr3 =~ /.*$ai6.*/)&&($nstr3 =~ /.*$ai7.*/)&&($max == length($key[$khit]))){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
}
$khit=$khit+1;
}
}


#/////////////////通常会話キーワードX1/////////////////////
if($hit== 0){

$nstr3="$str3$os";
$khit=0;
$max=0;
#---最長は何文字？---
while($key[$khit] ne ""){
if(($nstr3 =~ /$key[$khit]/)&&($max <= length($key[$khit]))){
$max=length($key[$khit]);
}
$khit=$khit+1;
}

#---最長のヒットの検索---
$khit=0;
while($key[$khit] ne ""){
if(($nstr3 =~ /$key[$khit]/)&&($max == length($key[$khit]))){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
$khit=$khit+1;
}
}


#//////通常会話キーワードX2(以前の会話も含めて検索)////////
if($hit== 0){

#---以前の会話も含めて検索---
$nstr3="$str3$kioku[$count]$kaitou[$count]$os";

#---最長は何文字？---
$khit=0;
$max=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /_/){
($ai6,$ai7)=split(/_/,$key[$khit]);
if(($nstr3 =~ /.*$ai6.*/)&&($nstr3 =~ /.*$ai7.*/)&&($max <= length($key[$khit]))){
$max=length($key[$khit]);
}
}
$khit=$khit+1;
}

#---ヒットの検索---
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /_/){
($ai6,$ai7)=split(/_/,$key[$khit]);
if(($nstr3 =~ /.*$ai6.*/)&&($nstr3 =~ /.*$ai7.*/)&&($max == length($key[$khit]))){
$oboe[$hit]=$oboe[$khit];
$kokoro[$hit]=$kokoro[$khit];
$kao[$hit]=$kao[$khit];
$hit=$hit+1;
}
}
$khit=$khit+1;
}
}


#/////////////////////呼んだ？/////////////////////////////
if($hit== 0){
if(($nstr3 =~ /EXA/)||($nstr3 =~ /草薙素子/)||($nstr3 =~ /えくさ/)||($nstr3 =~ /おまえ/)||($nstr3 =~ /お前/)||($nstr3 =~ /あなた/)||($nstr3 =~ /貴方/)||($nstr3 =~ /貴女/)||($nstr3 =~ /こいつ/)||($nstr3 =~ /君/)||($nstr3 =~ /キミ/)){
$oboe[$hit]="なに？";
$kao[$hit]=1;
$hit=1;
}
}


#///////////////////////口癖///////////////////////////////
if($hit== 0){
$oboe[$hit]="だって私、人工無脳ですから";
$kao[$hit]=12;
$hit=1;
$rand=int(rand(10));#---発生確率
if ($rand != 0){
$hit=0;
}
}


#/////////////////////状況判断/////////////////////////////
if($hit== 0){
open(joukyou,"<./dat/joukyou.dat");
while($joukyou=<joukyou>){
($joukyou2,$joukyou3,$joukyou4,$joukyou5)=split(/,/,$joukyou);
$ocount=0;
while($you[$ocount] ne ""){
if(($kioku[$ocount]=~/$joukyou2/)&&($itu[$ocount]=~/$logkyou/)){
$oboe[$hit]=$joukyou3;
$kokoro[$hit]=$joukyou4;
$kao[$hit]=$joukyou5;
$hit=$hit+1;
}
$ocount=$ocount+1;
}
}
$rand=int(rand(10));#---発生確率
if ($rand != 0){
$hit=0;
}
}


#///////////////////////独り言/////////////////////////////
if($hit == 0){
open(suki,"<./dat/suki.dat");
open(futuu,"<./dat/futuu.dat");
open(kirai,"<./dat/kirai.dat");

#---好きモード---
if($kimoti[$count] >=9){
#---好きデータ読み込み---
while($suki=<suki>){
($suki2,$suki3,$suki4)=split(/,/,$suki);
$oboe[$hit]=$suki2;
$kokoro[$hit]=$suki3;
$kao[$hit]=$suki4;
$hit=$hit+1;
}

#---嫌いモード---
} elsif ($kimoti[$count] <=3){
#---嫌いデータ読み込み---
while($kirai=<kirai>){
($kirai2,$kirai3,$kirai4)=split(/,/,$kirai);
$oboe[$hit]=$kirai2;
$kokoro[$hit]=$kirai3;
$kao[$hit]=$kirai4;
$hit=$hit+1;
}

#---普通モード--
} else {

#---普通データ読み込み---
while($futuu=<futuu>){
($futuu2,$futuu3,$futuu4)=split(/,/,$futuu);
$oboe[$hit]=$futuu2;
$kokoro[$hit]=$futuu3;
$kao[$hit]=$futuu4;
$hit=$hit+1;
}
}

#--ﾌｧｲﾙｸﾛｰｽﾞ---
close(suki);
close(futuu);
close(kirai);
}


#///////////////ヒットの中からランダムで選択///////////////
$hrand=int(rand($hit));



#〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜ループ防止します！〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜

#===前の会話と同じ言葉を繰り返さないよ===
$oboe[$hrand]=~ s/user/$yanata/g;#USERを貴方の名前に
if($kaitou[$count] eq $oboe[$hrand]){
if($hyoujou[$count]==0){
$hit=0;
$oboe[$hit]="そうね";
$kao[$hit]=0;
$hit=1;
} elsif ($hyoujou[$count]==1){
$hit=0;
$oboe[$hit]="そうだね";
$kao[$hit]=1;
$hit=1;
} elsif ($hyoujou[$count]==2){
$hit=0;
$oboe[$hit]="まったく";
$kao[$hit]=2;
$hit=1;
} elsif ($hyoujou[$count]==3){
$hit=0;
$oboe[$hit]="うう・・・";
$kao[$hit]=3;
$hit=1;
} elsif (($hyoujou[$count]==4)||($hyoujou[$count]==10)){
$hit=0;
$oboe[$hit]="あんたね";
$kao[$hit]=1;
$hit=1;
} elsif ($hyoujou[$count]==5){
$hit=0;
$oboe[$hit]="・・・user";
$kao[$hit]=5;
$hit=1;
} elsif ($hyoujou[$count]==6){
$hit=0;
$oboe[$hit]="ハハハ、それ駄目だって！";
$kao[$hit]=6;
$hit=1;
} elsif ($hyoujou[$count]==7){
$hit=0;
$oboe[$hit]="な！";
$kao[$hit]=7;
$hit=1;
} elsif ($hyoujou[$count]==9){
$hit=0;
$oboe[$hit]="user";
$kao[$hit]=0;
$hit=1;
} elsif ($hyoujou[$count]==11){
$hit=0;
$oboe[$hit]="困った人";
$kao[$hit]=11;
$hit=1;
} elsif ($hyoujou[$count]==12){
$hit=0;
$oboe[$hit]="ふふふ";
$kao[$hit]=12;
$hit=1;
}
#---ヒットの中からランダムで選択---
$hrand=int(rand($hit));
}

#〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜ループ防止します！ここまで〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜


}#***********************************************会話検索（$jump）終了************************************************************


#/////////////情報処理/////////////////////////////////////
#===あいさつ===
if(($ji>=4)&&($ji<=11)){
$aisatu="おはよう";
} elsif(($ji>=12)&&($ji<=16)){
$aisatu="こんにちは";
} elsif(($ji>=17)&&($ji<=23)){
$aisatu="こんばんは";
} elsif(($ji>=0)&&($ji<=3)){
$aisatu="こんばんは";
}
#===日にち===
#---何時間---
$ijikan="$ji時$fun分";
#---何日--
$initi="$tuki月$hi日";
#---何年---
$inen="$nen年";
#---平成---
$heisei1=$nen-1988;
$heisei="$heisei1年";
#---曜日---
@youbi_list=("日曜日","月曜日","火曜日","水曜日","木曜日","金曜日","土曜日");


#//////////////入れ替え////////////////////////////////////
#---何時間---
$oboe[$hrand]=~ s/jikan/$ijikan/g;
#---何日---
$oboe[$hrand]=~ s/niti/$initi/g;
#---何年--
$oboe[$hrand]=~ s/nen/$inen/g;
#---平成---
$oboe[$hrand]=~ s/heisei/$heisei/g;
#---曜日---
$oboe[$hrand]=~ s/youbi/$youbi_list[$youbi]/g;
#---あいさつ---
$oboe[$hrand]=~ s/aisatu/$aisatu/g;
#---会話の中に貴方の名前#---
$oboe[$hrand]=~ s/user/$yanata/g;


#////////////////////顔作成////////////////////////////////
@illust =("futuu.gif","tanosii.gif","akire.gif","kanasii.gif","ikari.gif","tere.gif","warai.gif","odoroki.gif","op.gif","ai.gif","tereikari.gif","ijiwaru.gif","egao.gif");

#===擬似感情コントロール===

#---デレ時の怒り、ツン時のテレ顔---
if(($kimoti[$count] >=9 && $kao[$hrand]==4) || ($kimoti[$count] <=3 && $kao[$hrand]==5)){
$skao[$hrand]=10;
}
#---デレ時の意地悪、ツン時の笑顔---
if(($kimoti[$count] >=9 && $kao[$hrand]==11) || ($kimoti[$count] <=3 && $kao[$hrand]==12)){
$skao[$hrand]=1;
}
#---テレた後の怒り顔---
if($hyoujou[$count]==5 && $kao[$hrand]==4){
$skao[$hrand]=10;
}
#---怒った後---
if($hyoujou[$count]==4){
$skao[$hrand]=10;
}
#---泣いた後の笑い顔---
if(($hyoujou[$count]==3 && $kao[$hrand]==1) || ($hyoujou[$count]==3 && $kao[$hrand]==6)){
$skao[$hrand]=12;
}

#---その他---
if($skao[$hrand]==0){
$skao[$hrand]=$kao[$hrand];
}


#////////////////////心の中////////////////////////////////
if($kokoro[$hrand] == 1){
$kimoti[$count]=$kimoti[$count]+1;
} elsif($kokoro[$hrand] == 2){
$kimoti[$count]=$kimoti[$count]-1;
}


#////////////////////心の中調整////////////////////////////
if ($kimoti[$count] >=11){
$kimoti[$count]=10;
} elsif ($kimoti[$count] <=0){
$kimoti[$count]=1;
}


#/////////////////心データ書き込み/////////////////////////
if ($anata1 ne ""){
open(kokoro,">>./dat/kokoro.dat");
print kokoro "\n$anata1,";
print kokoro "$kimoti[$count],";
print kokoro "$str3,";
print kokoro "$oboe[$hrand],";
$kao[$hrand]=~s/\n//g;
print kokoro "$kao[$hrand],";
print kokoro "$logkyou,";
$logjikan="$ji:$fun";
print kokoro "$logjikan";
close(kokoro);
}
#---現在のログは？---
open (kokoro,"<./dat/kokoro.dat");
$log=0;
while ($kokoro[$log] =<kokoro>){
$log=$log+1;
}
close (kokoro);

#---ログが5000を超えたら古いログ削除---
if ($log>5000){
open (kokoro,">./dat/kokoro.dat");
$dan=$log-5000;
while ($log != $dan){
print kokoro "$kokoro[$dan]";
$dan=$dan+1;
}
close (kokoro);
}

#////////////////＿html作成＿//////////////////////////////
$mydata  = Encode::decode("EUC-JP", $oboe[$hrand]);
$output  = Encode::encode("EUC-JP", $mydata);
print "Content-type: text/html; charset=EUC-JP \n\n";
print "$output";
exit;
