#!/usr/bin/perl

require 'jcode.pl';

print "Content-type: text/html; charset=EUC-JP \n\n";
print '<body background="kabe2.gif">';
print "<head>";
print "<title>���������ٶ�����</title>";
print "</head>";
print '<font color="#ffffff" size="3">';


#///////////////////////��������///////////////////////////
read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
$str =~ tr/+/ /;
$str =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
jcode::convert(*str,'euc');
($str2,$str3,$str4,$str5,$str6)=split(/&/,$str);

($ky,$ky2)=split(/=/,$str2);
($hennji,$hennji2)=split(/=/,$str3);
($suki,$suki2)=split(/=/,$str4);
($kao,$kao2)=split(/=/,$str5);
($kokoro1,$kokoro2)=split(/=/,$str6);


#//////////////////Ⱦ�ѥ������ʤ����Ѥˤ��ޤ�//////////////
jcode::h2z_euc(\$ky2);


####���ѱѿ���Ⱦ�ѱѿ��ˤ��ޤ�###############
$from = "���������������������������������"
       . "���£ãģţƣǣȣɣʣˣ̣ͣΣϣУѣңӣԣգ֣ףأ٣�"
       . "��������������������������������"
       . "!\"#%&'()+,:;<=>?\@[\\]`{|}~-";

$to = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         . "0123456789*./^_\$"
         . "���ɡ�����ǡʡˡܡ��������䡩��[��]�ơСáѡ���";

jcode::tr(\$ky2,$from, $to); 


#//////////////////��ʸ������ʸ����////////////////////////
$from = "abcdefghijklmnopqrstuvwxyz";
$to = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
jcode::tr(\$ky2,$from, $to); 


#*******************************�͹�̵Ǿ���������ޥå��󥰥��󥸥��$jump��***************************************

#---���Ϥʤ��Ƚ񤭹��ޤʤ���---
if($hennji2 ne ""){
if($kokoro2 == 0){
if($ky2 ne ""){
open(ai,">>./dat/ai.dat");
print ai"\n$ky2,";
print ai"$hennji2,";
print ai"$suki2,";
print ai"$kao2";
close(ai);
}

} elsif ($kokoro2 == 1){
open(futuu,">>./dat/futuu.dat");
print futuu"\n$hennji2,";
print futuu"$suki2,";
print futuu"$kao2";
close(futuu);

} elsif ($kokoro2 == 2){
open(suki,">>./dat/suki.dat");
print suki"\n$hennji2,";
print suki"$suki2,";
print suki"$kao2";
close(suki);

} elsif ($kokoro2 == 3){
open(kirai,">>./dat/kirai.dat");
print kirai"\n$hennji2,";
print kirai"$suki2,";
print kirai"$kao2";
close(kirai);

} elsif ($kokoro2 == 4){
if($ky2 ne ""){
open(event,">>./dat/event.dat");
print event"\n$ky2,";
print event"$hennji2,";
print event"$suki2,";
print event"$kao2";
close(event);
}
} elsif ($kokoro2 == 5){
if($ky2 ne ""){
open(joukyou,">>./dat/joukyou.dat");
print joukyou"\n$ky2,";
print joukyou"$hennji2,";
print joukyou"$suki2,";
print joukyou"$kao2";
close(joukyou);
}
}
}

#//////////////////////������Ÿ��//////////////////////////


print '<FORM ACTION="gakushuu.cgi" METHOD="POST">';
print 'ñ��򤤤�Ƥ�  ��(���ࡱo)<BR><BR>';
print '�������<INPUT TYPE="TEXT" NAME="name" SIZE="20"><BR>';
print '�ֻ�<INPUT TYPE="TEXT" NAME="name" SIZE="100"><BR>';
print "������ѥ�᡼����";
print "<BR>";
print '<input type="radio" name="kokoro"value="0" CHECKED>0_�դĤ�<BR>';
print '<INPUT TYPE="radio" name="kokoro"value="1">1_����<BR>';
print '<input type="radio" name="kokoro"value="2">2_���餤<BR>';
print "<BR>";
print "������";
print "<BR>";
print '<input type="radio" name=" kimoti"value="0" CHECKED>0_�դĤ�<BR>';
print '<input type="radio" name=" kimoti"value="1">1_�ڤ���<BR>';
print '<input type="radio" name=" kimoti"value="2">2_������<BR>';
print '<input type="radio" name=" kimoti"value="3">3_�ᤷ��<BR>';
print '<input type="radio" name=" kimoti"value="4">4_�ܤ�<BR>';
print '<input type="radio" name=" kimoti"value="5">5_�ƥ�<BR>';
print '<input type="radio" name=" kimoti"value="6">6_�Ф�<BR>';
print '<input type="radio" name=" kimoti"value="7">7_�ä�<BR>';
print '<input type="radio" name=" kimoti"value="9">9_����<BR>';
print '<input type="radio" name=" kimoti"value="11">11_�������<BR>';
print '<input type="radio" name=" kimoti"value="12">12_�д�<BR>';
print "<BR>";
print "����";
print "<BR>";
print '<input type="radio" name=" DATA"value="0" CHECKED>0_����<BR>';
print '<input type="radio" name=" DATA"value="1">1_����<BR>';
print '<input type="radio" name=" DATA"value="2">2_����<BR>';
print '<input type="radio" name=" DATA"value="3">3_����<BR>';
print '<input type="radio" name=" DATA"value="4">4_���٥��<BR>';
print '<input type="radio" name=" DATA"value="5">5_����<BR>';
print '<INPUT TYPE="SUBMIT" VALUE="����"><BR>';
print "<BR>";


#///////////////////////����///////////////////////////////
print '---������ˡ---<BR>';
print '���������ʤ����ѤǤ�<BR>';
print '��������ɤδ֤ˡ�_�פ�������2�������<BR>��������ɤκǽ�ˡ�EE�פ������ȥ������Τ��ȡ�MM�פ������Ȥ��ʤ��λ��ˤʤ�ޤ���<BR>';
print '���ֻ��ˡ�user�פ����Ϥ����̾����nen�פ����Ϥ����ǯ��jikan�פ����Ϥ���Ȼ��֡�niti�פ����Ϥ��������youbi�פ����Ϥ��������������ޤ���<BR>';
print '��������ɤˡ�__�פθ塢����Υ��������ֻ����ֻ��˼��˸������դǸ��⡼�ɤ�����ޤ���<BR>';
print '<BR>������ɽ���ε��ġ���ա�����ɽ���Τߤ����ϤϽ���ޤ����<BR>';
print '��������ɤ����ˡ�^�פ���Ƭ�ޥå���������ɤθ��ˡ�$�פǸ����ޥå�������ˡ�.*�פ�����θ��եޥå�<BR>';
print "<BR>";

#////////////////////////�ץ�ӥ塼////////////////////////
print "<BR>";
print "�������$str2";
print "<BR>";
print "�ֻ�$str3";
print "<BR>";
print "������$str4";
print "<BR>";
print "������$str5";
print "<BR>";
print "����$str6";
print "<BR>";
print '</font>';

exit;