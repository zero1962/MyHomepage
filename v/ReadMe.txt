【VRMLを用いたエアクラフト博物館(VRML Aircraft Museum)の構築】 2015.12.07 mon kuniyuki_tsujimoto

目的：やりたいことを明確にする。
--------------------------------------------------------
1. 【目標仕様】
(1) ３次元表示のエアクラフトをホームページで公開する。

2. 【仕様】
(1) VRML 2.0 形式でモデル表示する。
(2) モデルを選択したら、名称がでる。
(3) モデルをクリックしたら、wiki説明文がでる。もしくは、別窓で単体wrlが開く。

3. 【技術要素】
(1) VRML 2.0
(2) perl 5.8
(3) html
(4) FTP
(5) dnm->mqo->wrl 変換方法
(6) VRML 透明パーツ表示
(7) VRML 複数オブジェクト表示方法

4. 【作業項目】
(12) 残りのDnmをwrlに変換する。
(11) 土星、木星、火星、金星、水星、太陽を追加した。 2015.12.06
(10) 機体データをカテゴリ別フォルダに整理しなおした。
(9) 一部の機体に対してタッチ＆ゴーの簡易フライト表示を[FLY]で見れるようにした。
(8) [Wiki]リンクを追加した。
(7) Googleドライブに VRML Viewer を登録した。
(6) @nifty homepage をiPhone/iPad でも見えるように UTF-8 に変更した。
(5) dnm をwrl に変換する。
(4) 暫定ページアップロード　2015.11.22 済
(3) @nifty homepage を整理し Freeエリアを確保する。済　Free is 151MB = 300MB - 149MB 2015.11.22
(2) @nifty HP の　pc/ftp 接続を確立する。
(1) dnm を整理し、一覧表をつくる。 2015.11.22 済

5. 【問題点、修正箇所】
(1) fld をwrlに変換する方法を思い出せない。kobe.fld hnd.fldは実績があるのに。
(2) dnm著作権の確認が、数が多く作者がわからない。
    -> 謝辞を記載し問題あればメールしてもらうことにした。
(3) いくつかのモデルでマウス操作が、EXAMINE になっていないものがある。
(4) いくつかのモデルでヘッドライト設定が、TRUE になっていないものがある。

6. 【きっかけ】 2015.11.23 ｺﾞｰｽﾄの囁きがあった。
・YSFLIGHT に関連してVRML Viewr2.0 に付属してたコークスクリュー.wrl を見ていて思った。
・気が付くとYSFLIGHTのアドオン機体モデルを中心にたくさんの数があまっていた。
　世の中にこんなによくできた機体データがあるのにまったくうずもれていてもったいないと思った。
・YSFLIGHT のDNM形式では、ゲームでしか利用閲覧できないが、VRMLのwrl形式に変換すれば、Webブラウザで広く大勢の人に見てもらえる可能性が生まれる。
　VRML は、もう20年以上前に使い始めたが、今では、IEのプラグインもなくなってしまったが、今後、x3dに見直される可能性がある。
・dnm2mqo 変換perlスクリプトツールを朝飯中隊で発見した。（いま見つからない。）
・perl 5.10 以降は、Tk.pmがTkx.pm に大きく変更され古いスクリプトは使えなくなった。
・perl 5.20 が最新であり、古いバージョンは公式サイトで入手できないが、5.8を別途確保できた。
・Cyberdelia.exe でmqo2wrl できることを発見した。

7. 【参照サイト】
http://www.ysflight.com/   <-- 本家　YS Flight Simulator 山川機長のページ
http://ysfinder.net/       <-- 追加機体を探せます。
http://homepage3.nifty.com/k-tsujimoto/　　<-- 下名のページ

8.【今後の予定、希望】
・やっぱり機体操作させたい。
・鈴鹿サーキット、人工衛星、シャトル、セスナのモデル追加。
・あなたの好きなエアクラフトは何ですか？－＞Topの掲示板に書いてください。
・エドワード八木さんに紹介、＋林さん

9.【利用上の補足事項】
(1) VRML ビューワで見てください。
(2) 個々のファイル単位でもみれますが、VRML-Aircraft-Museumを開くと全体のオ
ブジェクトをみることができます。
(3) PageUp/PageDawn で視点を順番に変更できます。
(4) マウスの右クリックでも操作のキー指定を確認できます。

以上
------------------------END--




-----------------------------------
【YSFLIGHT dnm形式モデルからVRML wrl形式モデルに変換する手順】

F-22愛好会/朝飯中隊駐機場にあったperlスクリプトを用いる。
perlのﾊﾞｰｼﾞｮﾝは、5.8より後のﾊﾞｰｼﾞｮﾝは使えない。tk.pm -> tkx.pmに変わったため。

(1) trianglize.pl
・３種類のポリゴン調整をする。dnm->dnm： YS dnm形式

(2) dnm2mqo.pl
・STA でギミック選択する。脚だし等  dnm -> mqo ：メタセコイア形式

(3) Cyberdelia.exe
・法線、カメラ check ON  mqo -> wrl ：VRML形式

(4) エディタ
・.srf -> _srf に全置換する。
・透明部品に対して、shininessの後に以下を設定する。
	transparency 0.6
-----------------------------------
【ファイル構成】
C:\Users\kuro\Desktop\Myhomepage>tree /F > tree.txt
C:.
│  1.jpg
│  2.jpg
│  3.jpg
│  4.jpg
│  5.jpg
│  aclock.js
│  alarm.html
│  a_new.gif
│  bg.gif
│  bkg.gif
│  car1.gif
│  eaclock.js
│  eindex.html
│  ewhatsnew.txt
│  free_zero21.png
│  free_zero52h.png
│  heli_le.gif
│  heli_ri.gif
│  index.html
│  jpg.js
│  mylink.html
│  qreki.js
│  sendmail.html
│  today.js
│  tree.txt
│  uranai.html
│  WHATNEW.txt
│  zero.gif
│  zero.jpg
│
├─777
│      index.html
│
├─bio
│      bio.xls
│      index.html
│
├─fltsim
│      index.html
│
├─jpg
│      0.jpg
│      1.jpg
│      10.jpg
│      11.jpg
│      12.jpg
│      13.jpg
│      14.jpg
│      15.jpg
│      16.jpg
│      17.jpg
│      18.jpg
│      19.jpg
│      2.jpg
│      20.jpg
│      21.jpg
│      22.jpg
│      23.jpg
│      24.jpg
│      25.jpg
│      26.jpg
│      27.jpg
│      28.jpg
│      29.jpg
│      3.jpg
│      30.jpg
│      31.jpg
│      32.jpg
│      33.jpg
│      34.jpg
│      35.jpg
│      36.jpg
│      37.jpg
│      38.jpg
│      39.jpg
│      4.jpg
│      40.jpg
│      41.jpg
│      42.jpg
│      43.jpg
│      44.jpg
│      45.jpg
│      46.jpg
│      47.jpg
│      48.jpg
│      49.jpg
│      5.jpg
│      50.jpg
│      51.jpg
│      52.jpg
│      53.jpg
│      54.jpg
│      55.jpg
│      56.jpg
│      57.jpg
│      58.jpg
│      59.jpg
│      6.jpg
│      60.jpg
│      61.jpg
│      62.jpg
│      63.jpg
│      64.jpg
│      65.jpg
│      66.jpg
│      67.jpg
│      68.jpg
│      69.jpg
│      7.jpg
│      70.jpg
│      8.jpg
│      9.jpg
│
├─myhoby
│      index.html
│
├─myhoby2
│      index.html
│
├─myhoby3
│      index.html
│
├─myhoby4
│      index.html
│
├─o
│  │  index.html
│  │
│  └─fig
│          aki.png
│          black.png
│          Kblack.png
│          Kwhite.png
│          white.png
│
├─toyou
│      index.html
│
├─vrml
│  │  AirCract_Item_List.html
│  │  index.html
│  │  ReadMe.txt
│  │  ScreenShot.jpg
│  │  The Aircraft Museum by VRML 2.wrl
│  │  The Aircraft Museum by VRML.wrl
│  │
│  ├─AIRLINE
│  │  │  B747-OLDJAL.wrl
│  │  │  B747-OLDJAL_F.wrl
│  │  │  concorde.wrl
│  │  │  concorde2.wrl
│  │  │  concorde_F.wrl
│  │  │  mrj90.wrl
│  │  │  YS-11.wrl
│  │  │
│  │  └─concorde T
│  │          concorde.jpg
│  │          concorde.wrl
│  │          concorde_F.wrl
│  │
│  ├─Car
│  │      288gto.wrl
│  │      GTR-BLUE.wrl
│  │
│  ├─earth
│  │  │  e&m_mv.wrl
│  │  │  earth.jpg
│  │  │  earth.wrl
│  │  │  Sun.jpg
│  │  │
│  │  ├─Saturn
│  │  │      Ring.jpg
│  │  │      Saturn.jpg
│  │  │      Saturn.wrl
│  │  │
│  │  ├─Jupiter
│  │  │      Jupiter.jpg
│  │  │      Jupiter.wrl
│  │  │
│  │  ├─Mars
│  │  │      Mars.jpg
│  │  │      Mars.wrl
│  │  │
│  │  └─Moon
│  │          Moon.jpg
│  │          Moon.wrl
│  │          Moon2.jpg
│  │
│  ├─etc
│  │      Rider.wrl
│  │      Rider2.wrl
│  │      WrightFlyer.wrl
│  │
│  ├─Heli
│  │      sh60j.wrl
│  │
│  ├─JSDF
│  │      F-2A-525.wrl
│  │      F-2B 102 Gaer.wrl
│  │      f104J.wrl
│  │      f15j.wrl
│  │      f2a.wrl
│  │      f2aw.wrl
│  │      f2t.wrl
│  │      f4ejkai_423.wrl
│  │      s-Gear.wrl
│  │      us1a.wrl
│  │
│  ├─rv6a
│  │      desktop.ini
│  │      rv6a.wrl
│  │      rv6a_side.png
│  │      rv6a_Top_tpl.png
│  │
│  ├─Scenary
│  │      kobe.wrl
│  │      kobe2.wrl
│  │      kobe3.wrl
│  │      Tokyo.wrl
│  │      Tokyo2.wrl
│  │
│  ├─SF
│  │      frx00.wrl
│  │      mawe.wrl
│  │      Miku2.wrl
│  │      mk2.wrl
│  │      r2d2.wrl
│  │      savoia21.wrl
│  │      SP-yamato.wrl
│  │      tachikoma.wrl
│  │      y-Gear.wrl
│  │      Yakumo.png
│  │      yakumo_WFTC-F.wrl
│  │
│  ├─Ship
│  │      carrier.wrl
│  │      ibuki.wrl
│  │      mogami.wrl
│  │      shinano.wrl
│  │      takanami.wrl
│  │      yamato.wrl
│  │      yamato_b.wrl
│  │      yamato_d.wrl
│  │
│  ├─Space
│  │      h2a+ML.wrl
│  │      ISS.wrl
│  │      lunarlander.wrl
│  │
│  ├─Tank
│  │      90tk.wrl
│  │
│  ├─USA
│  │      F-15BN.wrl
│  │      F-22A.wrl
│  │      f15c-un.wrl
│  │      f35b.wrl
│  │      fa18.wrl
│  │
│  ├─WW I
│  │      dh82bl.wrl
│  │
│  ├─WW II
│  │      100tei3koug.wrl
│  │      1rk.wrl
│  │      1rk_F.wrl
│  │      2dai.wrl
│  │      2sui.wrl
│  │      96.wrl
│  │      97g.wrl
│  │      99.wrl
│  │      b29.wrl
│  │      b29_F.wrl
│  │      b7a2.wrl
│  │      d4y2.wrl
│  │      hien.wrl
│  │      p51d.wrl
│  │      reppu.wrl
│  │      seiran.wrl
│  │      shinden.wrl
│  │      spitfire21.wrl
│  │      z22.wrl
│  │      z22r.wrl
│  │      z52t.wrl
│  │      z52t_F.wrl
│  │
│  └─Zero-KT
│          cockpit.jpg
│          kt.jpg
│          Zero-KT.wrl
│
└─zii
        index.html

-----------------------------------
# VRML V2.0 utf8   記述サンプル
# Cyberdelia 6.6
# Takeshi Onishi
# http://www.cyberdelia.net/
# takeshi@cyberdelia.net

NavigationInfo {
	headlight TRUE
	visibilityLimit 100000.0
	type ["EXAMINE", "ANY"]
	avatarSize [0.25, 1.75, 0.75]
}

DEF all Transform {
	translation 0.0 0.0 0.0
	rotation  1.0 0.0 0.0 -0.2
	scale 1.0 1.0 1.0
	children [

# 機体データ
DEF T_0000(52body_srf) Transform {
	children [
	DEF RZ_0000(52body_srf) Transform {
	center 0.000000 0.000000 0.000000
	children [
	DEF RY_0000(52body_srf) Transform {
	center 0.000000 0.000000 0.000000
	children [
	DEF RX_0000(52body_srf) Transform {
	center 0.000000 0.000000 0.000000
	children [
	DEF S_0000(52body_srf) Transform {
	center 0.000000 0.000000 0.000000
	children [
#-------------------------------------
DEF PUSH_body TouchSensor {}
#-------------------------------------
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor 0.192000 0.290000 0.224000
					ambientIntensity 1.000000
					specularColor 0.000000 0.000000 0.000000
					emissiveColor 0.000000 0.000000 0.000000
					shininess 1.000000
				}
			}
			geometry IndexedFaceSet {
				coord Coordinate {
					point [
位置						0.399700 -0.021000 0.227500,
						0.238000 0.378000 -0.021000,
					]
				}
				coordIndex [
結線					2, 1, 0, -1,
					2003, 2002, 2001, -1,
				]
				normal Normal {
					vector [
						0.991970 -0.121157 -0.036295,
法線ベクトル					0.943560 0.330715 0.017926,
					]
				}
				normalIndex [
					2, 1, 0, -1,
					2003, 2002, 2001, -1,

				]
			}
		}
	]	}
	]	}
	]	}
	]	}
]	}
#-------------------------------------
DEF T_1003(tank2_srf) Transform {
DEF T_0001(eg_srf) Transform {
DEF T_0002(cwl-flap1-l_srf) Transform {
DEF T_0003(cwl-flap1-r_srf) Transform {
DEF T_0004(cwl-flap2-l_srf) Transform {
DEF T_0005(cwl-flap2-r_srf) Transform {
DEF T_0006(cwl-flap3-l_srf) Transform {
DEF T_0007(cwl-flap3-r_srf) Transform {
DEF T_0008(cwl-flap4-l_srf) Transform {
DEF T_0009(cwl-flap4-r_srf) Transform {
DEF T_0010(erlon-l_srf) Transform {
DEF T_0011(erlon-r_srf) Transform {
DEF T_0012(flap-l_srf) Transform {
DEF T_0013(flap-l-top_srf) Transform {
DEF T_0014(flap-r_srf) Transform {
DEF T_0015(flap-r-top_srf) Transform {
DEF T_0016(flapeg_srf) Transform {
DEF T_0017(rudder_srf) Transform {
DEF T_0018(ele_srf) Transform {
DEF T_00191(prop_srf) Transform {
DEF T_00192(prop_srf) Transform {
DEF T_00193(prop_srf) Transform {
DEF T_0020(maingr-l_srf) Transform {
DEF PUSH_gearL TouchSensor {}
DEF T_0021(maingr-r_srf) Transform {
DEF PUSH_gearR TouchSensor {}
DEF T_0022(maingrcovl-in_srf) Transform {
DEF T_0023(maingrcovl-out_srf) Transform {
DEF T_0024(maingrcovr-in_srf) Transform {
DEF T_0025(maingrcovr-out_srf) Transform {
DEF T_0026(maingrbox_srf) Transform {
DEF T_0027(tail-gr_srf) Transform {
DEF T_0028(tailbox_srf) Transform {
DEF T_0029(mark1_srf) Transform {
DEF T_0030(mark2_srf) Transform {
DEF T_0031(hook_srf) Transform {
DEF T_0032(pilot_srf) Transform {
DEF T_0033(cockpit_srf) Transform {
DEF T_0034(fcanopy_srf) Transform {
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor 0.514000 1.000000 1.000000
					ambientIntensity 1.000000
					specularColor 0.000000 0.000000 0.000000
					emissiveColor 0.000000 0.000000 0.000000
					shininess 1.000000
		                                  transparency 0.6
				}
			}
			geometry IndexedFaceSet {
				coord Coordinate {
					point [
						-0.111300 0.637000 -0.714000,
						0.128800 0.637700 -0.195300,
					]
				}
				coordIndex [
					2, 1, 0, -1,
					260, 259, 258, -1,
				]
				normal Normal {
					vector [
						-0.854966 0.511739 -0.084595,
						0.918673 0.393277 -0.037051,
					]
				}
				normalIndex [
					2, 1, 0, -1,
					260, 259, 258, -1,
				]
			}
		}
	]	}
	]	}
	]	}
	]	}
]	}
DEF T_0035(mcanopy_srf) Transform {
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor 0.514000 1.000000 1.000000
					ambientIntensity 1.000000
					specularColor 0.000000 0.000000 0.000000
					emissiveColor 0.000000 0.000000 0.000000
					shininess 1.000000
		                                  transparency 0.6
				}
			}
			geometry IndexedFaceSet {
				coord Coordinate {
					point [
						-0.053900 0.724500 -0.462000,
						-0.098700 0.693700 -0.444500,
					]
				}
				coordIndex [
					2, 1, 0, -1,
					95, 94, 93, -1,
				]
				normal Normal {
					vector [
						-0.402997 0.913940 -0.048032,
						-0.685111 0.728176 0.019563,
					]
				}
				normalIndex [
					2, 1, 0, -1,
					95, 94, 93, -1,
				]
			}
		}
	]	}
	]	}
	]	}
	]	}
]	}
DEF T_0037(propfast_srf) Transform {
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor 0.000000 0.643000 0.514000
					ambientIntensity 1.000000
					specularColor 0.000000 0.000000 0.000000
					emissiveColor 0.000000 0.000000 0.000000
					shininess 1.000000
                                  transparency 0.6
				}
			}
			geometry IndexedFaceSet {
				coord Coordinate {
					point [
						0.296100 -0.912100 1.393000,
						0.305200 0.938700 1.393000,
					]
				}
				coordIndex [
					2, 1, 0, -1,
					173, 172, 171, -1,
				]
				normal Normal {
					vector [
						-0.000000 -0.000000 1.000000,
						-0.000000 -0.000000 -1.000000,
					]
				}
				normalIndex [
					2, 1, 0, -1,
					173, 172, 171, -1,
				]
			}
		}
		Shape {
			appearance Appearance {
				material Material {
					diffuseColor 1.000000 0.000000 0.000000
					ambientIntensity 1.000000
					specularColor 0.000000 0.000000 0.000000
					emissiveColor 0.000000 0.000000 0.000000
					shininess 1.000000
                                  transparency 0.6
				}
			}
			geometry IndexedFaceSet {
				coord Coordinate {
					point [
						0.000000 0.987000 1.393000,
						-0.296100 0.912100 1.393000,
					]
				}
				coordIndex [
					2, 1, 0, -1,
					119, 118, 117, -1,
				]
				normal Normal {
					vector [
						-0.000000 -0.000000 -1.000000,
						-0.000000 -0.000000 1.000000,
					]
				}
				normalIndex [
					2, 1, 0, -1,
					119, 118, 117, -1,
				]
			}
		}
	]	}
	]	}
	]	}
	]	}
]	}
]
}

DEF OB_Camera Transform {
	translation -100.0 0.0 60.0
	rotation 0.0 1.0 0.0 -1.0
	scale 0.5 0.5 0.5
	children [
		DEF Camera Viewpoint {
			description "Ki-61 HIEN"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF OB_Camera6 Transform {
	translation 0.0 0.0 130.0
	rotation 0.0 1.0 0.0 0.0
	scale 1.0 1.0 1.0
	children [
		DEF Camera Viewpoint {
			description "Front view"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF OB_Camera5 Transform {
	translation 0.0 0.0 -130.0
	rotation 0.0 1.0 0.0 3.14
	scale 1.0 1.0 1.0
	children [
		DEF Camera Viewpoint {
			description "Rear view"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF OB_Camera4 Transform {
	translation 150.0 0.00 0.0
	rotation 0.0 1.0 0.0 1.57
	scale 1.0 1.0 1.0
	children [
		DEF Camera Viewpoint {
			description "Side view"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF OB_Camera3 Transform {
	translation 0.0 170.0 0.0
	rotation 1.0 0.0 0.0 -1.57
	scale 1.0 1.0 1.0
	children [
		DEF Camera Viewpoint {
			description "Top view"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF OB_Camera2 Transform {
	translation 0.0 6.5 -7.9
	rotation 0.0 1.0 0.0 3.14
	scale 1.0 1.0 1.0
	children [
		DEF Camera Viewpoint {
			description "Cockpit view"
			position 0.0 0.0 0.0
			orientation 0.0 0.0 0.0 0.0
			fieldOfView 0.661
		}
	]
}
DEF Time_gear TimeSensor
{
#	enabled TRUE
	loop FALSE
	startTime 0
	stopTime -1
	cycleInterval 1.0
}
ROUTE PUSH_gearR.isActive TO Time_gear.set_loop
DEF Anim_gdoorR OrientationInterpolator
{
	key      [ 0,      .33,       .66,        1.0 ]
	keyValue [
		0 0 1 0.0,
		0 0 1 -0.52,
		0 0 1 -1.05,
		0 0 1 -1.57 ]
}
DEF Anim_gdoorRP PositionInterpolator
{
	key      [ 0,      .33,       .66,        1.0 ]
	keyValue [
		 0.0   0.0   0.0,
		 0.1   -0.2   0.0,
		 0.2   -0.3   0.0,
		 0.3   -0.47  0.0 ]
}
ROUTE Time_gear.fraction_changed TO Anim_gdoorR.set_fraction
ROUTE Time_gear.fraction_changed TO Anim_gdoorRP.set_fraction
ROUTE Anim_gdoorR.value_changed TO T_0024(maingrcovr-in_srf).rotation
ROUTE Anim_gdoorRP.value_changed TO T_0022
(maingrcovr-in_srf).set_translation
-----------------------<END>------------
