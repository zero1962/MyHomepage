#!/usr/bin/perl

#
# EXA Android Program Vr1.34
#�ȥ�å�����Ǿ�ѡ���
#http://www.geocities.jp/tomock
#
require 'jcode.pl';
use Encode;
# use utf8;


#/////////////////////���ϼ�����/////////////////////////
read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
$str =~ tr/+/ /;
$str =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;

$str0 = Encode::decode("utf-8",  $str );
$str  = Encode::encode("EUC-JP", $str0);

($str1,$str2,$str3)=split(/=/,$str );
($anata1,$anata2)=split(/&/,$str2);


#//////////////////Ⱦ�ѥ������ʤ����Ѥˤ��ޤ�//////////////
jcode::h2z_euc(\$str3);


#//////////////////���ѱѿ���Ⱦ�ѱѿ��ˤ��ޤ�//////////////
$from = "���������������������������������"
       . "���£ãģţƣǣȣɣʣˣ̣ͣΣϣУѣңӣԣգ֣ףأ٣�"
       . "��������������������"
       . "!\"#\$%&'()*+,._/:;<=>?\@[\\]^`{|}~-";
$to = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         . "0123456789"
         . "���ɡ������ǡʡˡ��ܡ��������������䡩��[��]���ơСáѡ���";

jcode::tr(\$str3,$from, $to); 


#//////////////////��ʸ������ʸ����////////////////////////
$from = "abcdefghijklmnopqrstuvwxyz";
$to = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
jcode::tr(\$str3,$from, $to); 


#////////////////////////����//////////////////////////////
($byou,$fun,$ji,$hi,$tuki,$nen,$youbi,$yday,$sdst)=localtime(time);
$nen=$nen+1900;
$tuki=$tuki+1;


#///////////////////�פ��Ф��Ƥߤ��///////////////////////
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


#///////////////////////����/////////////////////////////
if($str3 eq ""){
$hrand=0;
$oboe[$hrand]="��ä��ꤷ�Ƥ��äƤ�";
$kao[$hrand]=12;
$jump=1;
}


#//////////////////////�ޤ���Ƥ��줿��////////////////////

#---���٥��---
$kyou="$tuki/$hi";
open(event,"<./dat/event.dat");
while($event=<event>){
($event2,$event3,$event4,$event5)=split(/,/,$event);
if ($event2 eq $kyou){
$event6=$event3;
}
}
close(event);

#---���㰧��---
$logkyou="$nen-$tuki-$hi";
if($itu[$count] !~ /$logkyou/){
$hrand=0;
if($kimoti[$count] >=9){
$oboe[$hrand]="user����Ƥ��줿��Ǥ���<BR>$event6";
$kao[$hrand]=0;
} elsif ($kimoti[$count] <=3){
$oboe[$hrand]="user���褿��<BR>$event6";
$kao[$hrand]=1;
} else {
$oboe[$hrand]="user��Ƥ��줿�����<BR>$event6";
$kao[$hrand]=1;
}
$jump=1;
}


#//////////////////////////���Ƥο�//////////////////////
if ($you[$count] eq ""){
$count=0;
$kimoti[$count] = 5;
$hrand=0;
$oboe[$hrand]="�Ϥ���ޤ���user��������͡�";
$kao[$hrand]=0;
$jump=1;
}


#//////////////////�����������////////////////////////////
$kersol="kaiwa";


#//////////////////̾�������ʤ���//////////////////////////
if($anata1 eq ""){
$kimoti[$count] = 10;
$hrand=0;
$oboe[$hrand]="̾�������Ϥ��Ƥ�������";
$kao[$hrand]=8;
$jump=1;
$kersol="name";#---�����������-----
}


#////////////////////���ʤ��θƤ���////////////////////////
if($kimoti[$count] >=9){
$yanata="$anata1";
} elsif ($kimoti[$count] <=3){
$yanata="$anata1";
} else {
$yanata="$anata1����";
}


if ($jump eq ""){#**********************�͹�̵Ǿ�����ǻҡ��ޥå��󥰥��󥸥��$jump��***************************************

#//////////////////�̾����ai.dat�ɤ߹���//////////////////
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


#////////////////////////////���//////////////////////////
if($hit== 0){
$khit=0;
while($key[$khit] ne ""){
if($key[$khit] =~ /__/){
$key[$khit]=~ s/__//g;
#�ҥåȤθ���
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


#////////////////////////�ޤͤ���ʡ�//////////////////////
if($hit== 0){
if($str3 eq $kaitou[$count]){
$oboe[$hit]="�ޡ��ޤͤ��ʤ��Ǥ��";
$kao[$hit]=10;
$kokoro[$hit]=0;
$hit=1;
}
}


#//////////////////////////���Ĥ����ʡ�////////////////////
if($hit== 0){
if(($str3 =~ /$kioku[$count]/)&&($str3 =~ /$kioku[$count-1]/)){
$oboe[$hit]="�⤦�����Ĥ�����";
$kao[$hit]=2;
$kokoro[$hit]=2;
$hit=1;
$oboe[$hit]="�ޤ����ä�";
$kao[$hit]=2;
$kokoro[$hit]=2;
$hit=2;
}
}


#///////////////////////ï�λ���///////////////////////////
if($hit== 0){
#---�����β��ä����¬---
#---�����ǻҤβ��ä���ͤ�ؤ����դ��ӽ�---
$dkaitou[$count]=$kaitou[$count];
$dkaitou[$count] =~ s/(EXA|�����ǻ�|������|���ޤ�|����|���ʤ�|����|����|������|��|����|��|����|��|�錄��|������|��ʬ|��|����|$anata1)//g;
$nstr3="$str3$kioku[$count]$dkaitou[$count]$os";

#---��������ǻҤλ�---
if(($nstr3 =~ /EXA/)||($nstr3 =~ /�����ǻ�/)||($nstr3 =~ /������/)||($nstr3 =~ /���ޤ�/)||($nstr3 =~ /����/)||($nstr3 =~ /���ʤ�/)||($nstr3 =~ /����/)||($nstr3 =~ /����/)||($nstr3 =~ /������/)||($nstr3 =~ /��/)||($nstr3 =~ /����/)){

#---��Ĺ�ϲ�ʸ����---
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

#---��Ĺ�ΥҥåȤθ���---
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

#---��줢�ʤ��λ�---
} elsif (($nstr3 =~ /��/)||($nstr3 =~ /����/)||($nstr3 =~ /��/)||($nstr3 =~ /�錄��/)||($nstr3 =~ /������/)||($nstr3 =~ /��ʬ/)||($nstr3 =~ /��/)||($nstr3 =~ /����/)||($nstr3 =~ /$anata1/)){

#---��Ĺ�ϲ�ʸ����---
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


#---��Ĺ�ΥҥåȤθ���---
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


#//////////////////�̾���å������X2////////////////////
if($hit== 0){
$nstr3="$str3$os";
$khit=0;
$max=0;
#---��Ĺ�ϲ�ʸ����---
while($key[$khit] ne ""){
if($key[$khit] =~ /_/){
($ai6,$ai7)=split(/_/,$key[$khit]);
if(($nstr3 =~ /.*$ai6.*/)&&($nstr3 =~ /.*$ai7.*/)&&($max <= length($key[$khit]))){
$max=length($key[$khit]);
}
}
$khit=$khit+1;
}

#---�ҥåȤθ���---
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


#/////////////////�̾���å������X1/////////////////////
if($hit== 0){

$nstr3="$str3$os";
$khit=0;
$max=0;
#---��Ĺ�ϲ�ʸ����---
while($key[$khit] ne ""){
if(($nstr3 =~ /$key[$khit]/)&&($max <= length($key[$khit]))){
$max=length($key[$khit]);
}
$khit=$khit+1;
}

#---��Ĺ�ΥҥåȤθ���---
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


#//////�̾���å������X2(�����β��ä�ޤ�Ƹ���)////////
if($hit== 0){

#---�����β��ä�ޤ�Ƹ���---
$nstr3="$str3$kioku[$count]$kaitou[$count]$os";

#---��Ĺ�ϲ�ʸ����---
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

#---�ҥåȤθ���---
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


#/////////////////////�Ƥ����/////////////////////////////
if($hit== 0){
if(($nstr3 =~ /EXA/)||($nstr3 =~ /�����ǻ�/)||($nstr3 =~ /������/)||($nstr3 =~ /���ޤ�/)||($nstr3 =~ /����/)||($nstr3 =~ /���ʤ�/)||($nstr3 =~ /����/)||($nstr3 =~ /����/)||($nstr3 =~ /������/)||($nstr3 =~ /��/)||($nstr3 =~ /����/)){
$oboe[$hit]="�ʤˡ�";
$kao[$hit]=1;
$hit=1;
}
}


#///////////////////////����///////////////////////////////
if($hit== 0){
$oboe[$hit]="���äƻ䡢�͹�̵Ǿ�Ǥ�����";
$kao[$hit]=12;
$hit=1;
$rand=int(rand(10));#---ȯ����Ψ
if ($rand != 0){
$hit=0;
}
}


#/////////////////////����Ƚ��/////////////////////////////
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
$rand=int(rand(10));#---ȯ����Ψ
if ($rand != 0){
$hit=0;
}
}


#///////////////////////�Ȥ��/////////////////////////////
if($hit == 0){
open(suki,"<./dat/suki.dat");
open(futuu,"<./dat/futuu.dat");
open(kirai,"<./dat/kirai.dat");

#---�����⡼��---
if($kimoti[$count] >=9){
#---�����ǡ����ɤ߹���---
while($suki=<suki>){
($suki2,$suki3,$suki4)=split(/,/,$suki);
$oboe[$hit]=$suki2;
$kokoro[$hit]=$suki3;
$kao[$hit]=$suki4;
$hit=$hit+1;
}

#---�����⡼��---
} elsif ($kimoti[$count] <=3){
#---�����ǡ����ɤ߹���---
while($kirai=<kirai>){
($kirai2,$kirai3,$kirai4)=split(/,/,$kirai);
$oboe[$hit]=$kirai2;
$kokoro[$hit]=$kirai3;
$kao[$hit]=$kirai4;
$hit=$hit+1;
}

#---���̥⡼��--
} else {

#---���̥ǡ����ɤ߹���---
while($futuu=<futuu>){
($futuu2,$futuu3,$futuu4)=split(/,/,$futuu);
$oboe[$hit]=$futuu2;
$kokoro[$hit]=$futuu3;
$kao[$hit]=$futuu4;
$hit=$hit+1;
}
}

#--�̎����َ��ێ�����---
close(suki);
close(futuu);
close(kirai);
}


#///////////////�ҥåȤ��椫������������///////////////
$hrand=int(rand($hit));



#���������������������������������������롼���ɻߤ��ޤ�����������������������������������������������

#===���β��ä�Ʊ�����դ򷫤��֤��ʤ���===
$oboe[$hrand]=~ s/user/$yanata/g;#USER������̾����
if($kaitou[$count] eq $oboe[$hrand]){
if($hyoujou[$count]==0){
$hit=0;
$oboe[$hit]="������";
$kao[$hit]=0;
$hit=1;
} elsif ($hyoujou[$count]==1){
$hit=0;
$oboe[$hit]="��������";
$kao[$hit]=1;
$hit=1;
} elsif ($hyoujou[$count]==2){
$hit=0;
$oboe[$hit]="�ޤä���";
$kao[$hit]=2;
$hit=1;
} elsif ($hyoujou[$count]==3){
$hit=0;
$oboe[$hit]="����������";
$kao[$hit]=3;
$hit=1;
} elsif (($hyoujou[$count]==4)||($hyoujou[$count]==10)){
$hit=0;
$oboe[$hit]="���󤿤�";
$kao[$hit]=1;
$hit=1;
} elsif ($hyoujou[$count]==5){
$hit=0;
$oboe[$hit]="������user";
$kao[$hit]=5;
$hit=1;
} elsif ($hyoujou[$count]==6){
$hit=0;
$oboe[$hit]="�ϥϥϡ��������ܤ��äơ�";
$kao[$hit]=6;
$hit=1;
} elsif ($hyoujou[$count]==7){
$hit=0;
$oboe[$hit]="�ʡ�";
$kao[$hit]=7;
$hit=1;
} elsif ($hyoujou[$count]==9){
$hit=0;
$oboe[$hit]="user";
$kao[$hit]=0;
$hit=1;
} elsif ($hyoujou[$count]==11){
$hit=0;
$oboe[$hit]="���ä���";
$kao[$hit]=11;
$hit=1;
} elsif ($hyoujou[$count]==12){
$hit=0;
$oboe[$hit]="�դդ�";
$kao[$hit]=12;
$hit=1;
}
#---�ҥåȤ��椫������������---
$hrand=int(rand($hit));
}

#�������������������������������������롼���ɻߤ��ޤ��������ޤǡ�����������������������������������������


}#***********************************************���ø�����$jump�˽�λ************************************************************


#/////////////�������/////////////////////////////////////
#===��������===
if(($ji>=4)&&($ji<=11)){
$aisatu="���Ϥ褦";
} elsif(($ji>=12)&&($ji<=16)){
$aisatu="����ˤ���";
} elsif(($ji>=17)&&($ji<=23)){
$aisatu="����Ф��";
} elsif(($ji>=0)&&($ji<=3)){
$aisatu="����Ф��";
}
#===���ˤ�===
#---������---
$ijikan="$ji��$funʬ";
#---����--
$initi="$tuki��$hi��";
#---��ǯ---
$inen="$nenǯ";
#---ʿ��---
$heisei1=$nen-1988;
$heisei="$heisei1ǯ";
#---����---
@youbi_list=("������","������","������","������","������","������","������");


#//////////////�����ؤ�////////////////////////////////////
#---������---
$oboe[$hrand]=~ s/jikan/$ijikan/g;
#---����---
$oboe[$hrand]=~ s/niti/$initi/g;
#---��ǯ--
$oboe[$hrand]=~ s/nen/$inen/g;
#---ʿ��---
$oboe[$hrand]=~ s/heisei/$heisei/g;
#---����---
$oboe[$hrand]=~ s/youbi/$youbi_list[$youbi]/g;
#---��������---
$oboe[$hrand]=~ s/aisatu/$aisatu/g;
#---���ä���˵�����̾��#---
$oboe[$hrand]=~ s/user/$yanata/g;


#////////////////////�����////////////////////////////////
@illust =("futuu.gif","tanosii.gif","akire.gif","kanasii.gif","ikari.gif","tere.gif","warai.gif","odoroki.gif","op.gif","ai.gif","tereikari.gif","ijiwaru.gif","egao.gif");

#===�������𥳥�ȥ���===

#---�ǥ�����ܤꡢ�ĥ���Υƥ��---
if(($kimoti[$count] >=9 && $kao[$hrand]==4) || ($kimoti[$count] <=3 && $kao[$hrand]==5)){
$skao[$hrand]=10;
}
#---�ǥ���ΰ��ϰ����ĥ���ξд�---
if(($kimoti[$count] >=9 && $kao[$hrand]==11) || ($kimoti[$count] <=3 && $kao[$hrand]==12)){
$skao[$hrand]=1;
}
#---�ƥ줿����ܤ��---
if($hyoujou[$count]==5 && $kao[$hrand]==4){
$skao[$hrand]=10;
}
#---�ܤä���---
if($hyoujou[$count]==4){
$skao[$hrand]=10;
}
#---�㤤����ξФ���---
if(($hyoujou[$count]==3 && $kao[$hrand]==1) || ($hyoujou[$count]==3 && $kao[$hrand]==6)){
$skao[$hrand]=12;
}

#---����¾---
if($skao[$hrand]==0){
$skao[$hrand]=$kao[$hrand];
}


#////////////////////������////////////////////////////////
if($kokoro[$hrand] == 1){
$kimoti[$count]=$kimoti[$count]+1;
} elsif($kokoro[$hrand] == 2){
$kimoti[$count]=$kimoti[$count]-1;
}


#////////////////////������Ĵ��////////////////////////////
if ($kimoti[$count] >=11){
$kimoti[$count]=10;
} elsif ($kimoti[$count] <=0){
$kimoti[$count]=1;
}


#/////////////////���ǡ����񤭹���/////////////////////////
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
#---���ߤΥ��ϡ�---
open (kokoro,"<./dat/kokoro.dat");
$log=0;
while ($kokoro[$log] =<kokoro>){
$log=$log+1;
}
close (kokoro);

#---����5000��Ķ������Ť������---
if ($log>5000){
open (kokoro,">./dat/kokoro.dat");
$dan=$log-5000;
while ($log != $dan){
print kokoro "$kokoro[$dan]";
$dan=$dan+1;
}
close (kokoro);
}

#////////////////��html������//////////////////////////////
$mydata  = Encode::decode("EUC-JP", $oboe[$hrand]);
$output  = Encode::encode("EUC-JP", $mydata);
print "Content-type: text/html; charset=EUC-JP \n\n";
print "$output";
exit;
