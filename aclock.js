//
//        アナログ時計
// 
centerx=450;                       //表示位置横
centery=300;                       //表示位置縦
mojicolor="#0000ff";               //数字の色
mojisize=24;                       //数字の大きさ
tencolor="#0000ff";                //中心点の色
tensize=32;                        //中心点の大きさ
encolor="#77ffff";                 //背景点の色
ensize=400;                        //背景点の大きさ
Hcolor="#9900ff";                  //短針の色
Mcolor="#cc00ff";                  //長針の色
Scolor="#000000";                  //秒針の色
Hspan=7;                           //短針の・と・の間隔
Mspan=7;                           //長針の・と・の間隔
Sspan=7;                           //秒針の・と・の間隔
Hsize=14;                          //短針の・の大きさ
Msize=10;                          //長針の・の大きさ
Ssize=8;                           //秒針の・の大きさ
diamete=70;                        //半径
//---------------------------------------------------  

jikan=2;
document.write("<DIV STYLE='position:absolute;font-size:"+ensize+";top:"+(centery*0.87-ensize/2)+";left:"+(centerx*1.178-ensize/2)+";color:"+encolor+"'>●</DIV>");
for(i=0;i<12;i++)
{
	staX=centerx + Math.cos(Math.PI*2/12*(i+1))*diamete;
	staY=centery + Math.sin(Math.PI*2/12*(i+1))*diamete;
	jikan++;jikan%=12;
	document.write("<DIV STYLE='position:absolute;font:"+mojisize+" Times New Roman;top:"+(staY-6)+";left:"+(staX-6)+";color:"+mojicolor+"'><b>"+(jikan+1)+"</b></DIV>");
}
for(i=0;i<10;i++)
{
	document.write("<DIV STYLE='position:absolute;font-size:"+Msize+";top:"+centery+";left:"+centerx+";color:"+Mcolor+"'ID='M"+i+"'>●</DIV>");
	document.write("<DIV STYLE='position:absolute;font-size:"+Ssize+";top:"+centery+";left:"+centerx+";color:"+Scolor+"'ID='S"+i+"'>●</DIV>");
	if(i<7)document.write("<DIV STYLE='position:absolute;font-size:"+Hsize+";top:"+centery+";left:"+centerx+";color:"+Hcolor+"'ID='H"+i+"'>●</DIV>");
}
document.write("<DIV STYLE='position:absolute;font-size:"+tensize+";top:"+(centery*1.01-tensize/2)+";left:"+(centerx*1.018-tensize/2)+";color:"+tencolor+"'>●</DIV>");
function Nowtime()
{
	Now=new Date();
	S=Now.getSeconds()-15;
	M=Now.getMinutes()+45;
	H=(Now.getHours()+9)+(Now.getMinutes()/60);
	for(i=0;i<10;i++)
	{
		funX=centerx + Math.cos(Math.PI*2/60*M)*(i*Mspan+Mspan);
		funY=centery + Math.sin(Math.PI*2/60*M)*(i*Mspan+Mspan);
		byouX=centerx + Math.cos(Math.PI*2/60*S)*(i*Sspan+Sspan);
		byouY=centery + Math.sin(Math.PI*2/60*S)*(i*Sspan+Sspan);
		if(document.all)
		{
			document.all("M"+i).style.pixelLeft = funX;
			document.all("M"+i).style.pixelTop = funY;
			document.all("S"+i).style.pixelLeft = byouX;
			document.all("S"+i).style.pixelTop = byouY;
		}
		else
		{
			document.getElementById("M"+i).style.left = funX;
			document.getElementById("M"+i).style.top = funY;
			document.getElementById("S"+i).style.left = byouX;
			document.getElementById("S"+i).style.top = byouY;
		}
		if(i > 6)continue;
		hourX=centerx + Math.cos(Math.PI*2/12*H)*(i*Hspan+Hspan);
		hourY=centery + Math.sin(Math.PI*2/12*H)*(i*Hspan+Hspan);
		if(document.all)
		{
			document.all("H"+i).style.pixelLeft = hourX;
			document.all("H"+i).style.pixelTop = hourY;
		}
		else
		{
			document.getElementById("H"+i).style.left = hourX;
			document.getElementById("H"+i).style.top  = hourY;
		}
	}
}
setInterval("Nowtime()",1000);/* himajin.moo.jp */
