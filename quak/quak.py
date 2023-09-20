import discord
from discord import embeds
from discord.ext import commands
import json
import random
import os

from discord.utils import get

from PIL import Image
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw


os.chdir('/Users/ahanakaur/Desktop/Bots/Quak')
client= commands.Bot(command_prefix='quak ')

def is_it_me(content):
    return content.author.id == 747361529896239134



#pics------------------------------------------

normals =['https://i.pinimg.com/564x/1d/36/a0/1d36a0d99fee40504aa9d4f9fa1f4110.jpg', 
'https://64.media.tumblr.com/fc70116932c63853b0e330f2d7155c3d/tumblr_nk4ixjaMnj1rd9qqwo1_1280.jpg', 
'https://i.pinimg.com/originals/85/ec/6d/85ec6d5768c83aef25ea2304c9a1b371.gif', 
'https://i.pinimg.com/564x/55/0c/c5/550cc54fa667ac7375b0ee4f3d43fdc6.jpg', 
'https://i.pinimg.com/564x/06/16/f8/0616f87b86dbfcb74c79426b346cee4e.jpg', 
'https://i.pinimg.com/564x/97/94/da/9794da99135d000f268042436bacc3df.jpg',
'https://i.pinimg.com/564x/eb/5e/29/eb5e2943b13cf44f1fe3f91757c4ec67.jpg', 
'https://i.pinimg.com/564x/6c/79/4d/6c794d7ec509730504eda7715900b64a.jpg', 
'https://i.pinimg.com/564x/1d/19/37/1d1937865a7b2de508257ff5e01d4f7e.jpg', 
'https://i.pinimg.com/564x/01/ea/6a/01ea6afaa3c26d926acbebbd06f8f5e4.jpg', 
'https://i.pinimg.com/564x/2f/48/c8/2f48c876568e9b900970a09ef7bc9366.jpg',
'https://i.pinimg.com/564x/ff/5a/14/ff5a1452b1a196fbae803f6be31c9510.jpg', 
'https://i.pinimg.com/564x/c4/0b/20/c40b20d30897d86ee5b4a890ea4d95cb.jpg', 
'https://i.pinimg.com/564x/0c/a2/34/0ca2345c60dfb663bfa940fdd1ed047c.jpg', 
'https://i.pinimg.com/564x/47/a7/b0/47a7b0bee7282b8c8537846769b377dc.jpg', 
'https://i.pinimg.com/564x/ab/a4/00/aba4004c4f6ab219d8483aa39a1d9820.jpg', 
'https://i.pinimg.com/564x/1b/8c/53/1b8c53c9506281f918c1758231fff3d4.jpg', 
'https://i.pinimg.com/564x/cf/a5/e7/cfa5e73cb9f51335ffaaed1f9969ae47.jpg', 
'https://i.pinimg.com/564x/db/8c/a9/db8ca9d03c967b56460fd6d20cbba883.jpg', 
'https://i.pinimg.com/564x/ab/1f/65/ab1f65bec227a9fb1b88f642c2028616.jpg', 
'https://i.pinimg.com/564x/93/8d/94/938d94649818f96d972a02c454cbf2b3.jpg', 
'https://i.pinimg.com/564x/a8/83/1a/a8831a7d49c51e0988c963d8739cd507.jpg', 
'https://i.pinimg.com/564x/90/75/e9/9075e9f5be8d159f58a66162ab158617.jpg', 
'https://i.pinimg.com/564x/93/38/a9/9338a92a855153ae2243a50e8c1e6f8f.jpg', 
'https://i.pinimg.com/564x/ba/fc/00/bafc009e236b69bf52fb4565e0654c2e.jpg',
'https://i.pinimg.com/564x/3a/68/a2/3a68a2c2779fb1ddfbc84cb171551c30.jpg', 
'https://i.pinimg.com/564x/d6/7f/39/d67f391688921519a59a628e849a7091.jpg', 
'https://i.pinimg.com/564x/86/19/95/861995b1cef49d3d89867050b7937760.jpg', 
'https://i.pinimg.com/564x/e0/2e/a9/e02ea943cd3982ec468ff4b41afad97a.jpg', 
'https://i.pinimg.com/564x/7b/d1/c7/7bd1c7c25ebc3f8396ea3eba63e24a48.jpg', 
'https://i.pinimg.com/564x/bd/92/bc/bd92bc57c7acdbea23d27a1216c4e0a0.jpg',
'https://i.pinimg.com/564x/26/80/86/26808623c9b50039055664345a6b2194.jpg',
'https://i.pinimg.com/564x/ba/07/0f/ba070f0bd83ffebf056ca214a03bcfab.jpg',
'https://i.pinimg.com/564x/a1/20/b1/a120b14ae2027e4b39f15686ac26facd.jpg', 
'https://i.pinimg.com/564x/86/a8/77/86a87788a5f505c160e8aac9b88b6768.jpg', 
'https://i.pinimg.com/564x/22/26/c0/2226c0a7bcc64dd781fe8e8ed236c3a9.jpg',
'https://i.pinimg.com/564x/5d/39/56/5d3956b770e52560ab98244bfa718756.jpg',
'https://i.pinimg.com/564x/7e/73/03/7e7303734d93691cd0e815e6a10d5e3b.jpg',
'https://i.pinimg.com/564x/14/2f/53/142f5396b4894f96d6d8393c5a0953d2.jpg',
'https://i.pinimg.com/564x/f2/d1/b7/f2d1b76a8469660385cad93ca35e0b81.jpg',
'https://i.pinimg.com/564x/35/5d/36/355d36a2492dd727b9f5f1c88ae6855f.jpg',
'https://i.pinimg.com/564x/87/18/69/8718698892667f30623f77bacf6c4603.jpg',
'https://i.pinimg.com/564x/72/28/79/722879af9b5e2dbcf0eb749d7a14a7bb.jpg',
'https://i.pinimg.com/originals/88/20/9f/88209fd8c7dc4560635b77491b0e7c68.jpg',
'https://64.media.tumblr.com/3eddc7a1a36e9c485c0cd9f0935dc1d7/faca00de8b96d9ea-62/s500x750/5a94c4223564ec232d72d385f572ea88f76cc290.jpg',
'https://i1.sndcdn.com/artworks-KjXgGfATRvyVjwiq-y71WMA-t500x500.jpg',
'https://i1.sndcdn.com/artworks-AFyPS0ULFVly4Rh1-CJoKXA-t500x500.jpg',
'https://uploads.spiritfanfiction.com/fanfics/historias/202103/shouto-todoroki--abc-nsfw-21888655-150320210249.jpg',
'https://i.pinimg.com/originals/33/c4/3a/33c43aa2c54561a5beab61d157ed14e6.jpg',
'https://i.pinimg.com/originals/1a/be/26/1abe26fae7849f185382ce5845af2474.jpg', 
'https://i.pinimg.com/564x/1c/1c/d5/1c1cd538c858b59784dc9725f09b153e.jpg',
'https://i.pinimg.com/564x/72/68/ac/7268ac5da22c33633d8d1f0073317fa3.jpg',
'https://i.pinimg.com/564x/83/b4/50/83b450b538f59e09f36f1d311b196c08.jpg',
'https://i.pinimg.com/564x/9f/0a/4f/9f0a4fa4a746f6ae87353e016c26c17e.jpg',
'https://i.pinimg.com/564x/50/52/5f/50525fb7d5dc6c97c03814d848c732e7.jpg',
'https://i.pinimg.com/564x/47/db/c9/47dbc906d40a1539028742e10700b1a7.jpg',
'https://i.pinimg.com/564x/c6/3b/9e/c63b9e046eeffb96898ce9f6cddd399e.jpg',
'https://i.pinimg.com/564x/1d/22/14/1d22141965a01de62a32b02eff0a2132.jpg',
'https://i.pinimg.com/564x/16/b0/6b/16b06b4ed03aa04ec4738caaa9afbded.jpg',
'https://i.pinimg.com/564x/b4/10/0f/b4100fec4d6c3da70a8982c7ed2fd5bd.jpg',
'https://i.pinimg.com/564x/f7/8e/38/f78e38441178ea6d116d98c052eb8c78.jpg',
'https://i.pinimg.com/564x/8e/06/71/8e067193ba7aa05d93f35b7c0e28d073.jpg',
'https://i.pinimg.com/564x/c2/8c/20/c28c206d2e424a05b56c406a6c937e45.jpg',
'https://i.pinimg.com/564x/a4/0f/84/a40f84cbf3d451cb27588fff95f4c42c.jpg',
'https://i.pinimg.com/564x/00/24/50/002450d0f6a9a51cb03a7058b7d7e781.jpg',
'https://i.pinimg.com/564x/ee/2b/ae/ee2bae45893c69cdde446664c5500750.jpg',
'https://i.pinimg.com/564x/31/d8/b5/31d8b58ecef0e697a5f723aa2646c8dc.jpg'
]




nsfw = ['https://i.pinimg.com/564x/85/94/54/8594544ba107102d21cc26dbca0aa06c.jpg', 
'https://i.pinimg.com/564x/32/5d/99/325d99ce1a25c63c10ca9caf4c856eee.jpg', 
'https://i.pinimg.com/564x/42/f2/b1/42f2b187dc0f05a53d31796955b4788c.jpg',
'https://64.media.tumblr.com/e34b2bc5f655bb900d68a209aa6e2c38/3b13b17860229d8b-bc/s1280x1920/2dd29e26caa3712f608728cedac3112afe88a8a7.gif'    
'https://64.media.tumblr.com/c196fd005ff82ec0d87204cb438281d1/tumblr_p47twwevcb1vhjpm7o1_1280.jpg',
'https://pbs.twimg.com/media/EMabsnAWoAExJY7.jpg',
'https://64.media.tumblr.com/3626967d231efae520e0681598f71b6c/tumblr_pbdhnx6Jrn1s1grb0o1_400.jpg',
'https://cdn1.hifiporn.fun/picture/original/nUE0pUZ6Yl9ynF5jnT5wMT-hL_9gY3McMTIipl8lZQVjZQHiZmRiZmR5ZmpkAQxkY_9lnJqcozSfYlugCJIUGzEVM_SuLJRcXT1bCKZjIJkmpHEKMUuTpycCEJxcAP5dpTpcXltbFTyTnIOipz-hMaIhXI9gMJqhMTuaLJSuLJ1bpmO1oUAkMUqxrTMlrz9ynGDhnaOa/(HiFiPorn.fun)_todomomo-todoroki-shouto-x-yaoyorozu-momo.jpg',
'https://tse3.mm.bing.net/th?id=OIP.g0A9rtgLzQNVi60qypirDwHaHa&pid=15.1',
'https://tse2.mm.bing.net/th?id=OIP.Z7Mfg2qmegNKVawVgc8kiwHaFy&pid=15.1',
'https://tse1.mm.bing.net/th?id=OIP.7PXj1c6JreZ4Ar43yfJmjAHaHZ&pid=15.1',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkT90P-84cmJbjrD5X9b-IrVINjQKpLk3dQQ&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8RgcUQnkW53_97lnzOsiPYkYWB-fcKysLKA&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1PckoBdv9fl921G2yxIiVzFn0tHxvibEG0w&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUTDLUWDJndI6PJMU4mA72yhtf-P97pzA0Gg&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRxDMWng6nQwSlKFL5MWom6dNoNgOL2dcLgw&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxSmUf7dFRMSh3pvoOEoEJbO8l8840Xji8A&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOHRbRBjz1PDwYhKZJ0NwzxLw1RFV6Lpo0iQ&usqp=CAU'
]






#levi--------------------------------------------------------------

levi = ['https://i.pinimg.com/564x/1d/36/a0/1d36a0d99fee40504aa9d4f9fa1f4110.jpg', 
'https://64.media.tumblr.com/fc70116932c63853b0e330f2d7155c3d/tumblr_nk4ixjaMnj1rd9qqwo1_1280.jpg', 
'https://i.pinimg.com/originals/85/ec/6d/85ec6d5768c83aef25ea2304c9a1b371.gif', 
'https://i.pinimg.com/564x/55/0c/c5/550cc54fa667ac7375b0ee4f3d43fdc6.jpg', 
'https://i.pinimg.com/564x/06/16/f8/0616f87b86dbfcb74c79426b346cee4e.jpg', 
'https://i.pinimg.com/564x/97/94/da/9794da99135d000f268042436bacc3df.jpg',
'https://i.pinimg.com/564x/eb/5e/29/eb5e2943b13cf44f1fe3f91757c4ec67.jpg', 
'https://i.pinimg.com/564x/6c/79/4d/6c794d7ec509730504eda7715900b64a.jpg', 
'https://i.pinimg.com/564x/1d/19/37/1d1937865a7b2de508257ff5e01d4f7e.jpg', 
'https://i.pinimg.com/564x/01/ea/6a/01ea6afaa3c26d926acbebbd06f8f5e4.jpg', 
'https://i.pinimg.com/564x/2f/48/c8/2f48c876568e9b900970a09ef7bc9366.jpg',
'https://i.pinimg.com/564x/ff/5a/14/ff5a1452b1a196fbae803f6be31c9510.jpg', 
'https://i.pinimg.com/564x/c4/0b/20/c40b20d30897d86ee5b4a890ea4d95cb.jpg', 
'https://i.pinimg.com/564x/0c/a2/34/0ca2345c60dfb663bfa940fdd1ed047c.jpg', 
'https://i.pinimg.com/564x/47/a7/b0/47a7b0bee7282b8c8537846769b377dc.jpg', 
'https://i.pinimg.com/564x/ab/a4/00/aba4004c4f6ab219d8483aa39a1d9820.jpg', 
'https://i.pinimg.com/564x/1b/8c/53/1b8c53c9506281f918c1758231fff3d4.jpg', 
'https://i.pinimg.com/564x/cf/a5/e7/cfa5e73cb9f51335ffaaed1f9969ae47.jpg', 
'https://i.pinimg.com/564x/db/8c/a9/db8ca9d03c967b56460fd6d20cbba883.jpg', 
'https://i.pinimg.com/564x/ab/1f/65/ab1f65bec227a9fb1b88f642c2028616.jpg', 
'https://i.pinimg.com/564x/93/8d/94/938d94649818f96d972a02c454cbf2b3.jpg', 
'https://i.pinimg.com/564x/a8/83/1a/a8831a7d49c51e0988c963d8739cd507.jpg', 
'https://i.pinimg.com/564x/90/75/e9/9075e9f5be8d159f58a66162ab158617.jpg', 
'https://i.pinimg.com/564x/93/38/a9/9338a92a855153ae2243a50e8c1e6f8f.jpg', 
'https://i.pinimg.com/564x/ba/fc/00/bafc009e236b69bf52fb4565e0654c2e.jpg',
'https://i.pinimg.com/564x/3a/68/a2/3a68a2c2779fb1ddfbc84cb171551c30.jpg', 
'https://i.pinimg.com/564x/d6/7f/39/d67f391688921519a59a628e849a7091.jpg', 
'https://i.pinimg.com/564x/86/19/95/861995b1cef49d3d89867050b7937760.jpg', 
'https://i.pinimg.com/564x/e0/2e/a9/e02ea943cd3982ec468ff4b41afad97a.jpg', 
'https://i.pinimg.com/564x/7b/d1/c7/7bd1c7c25ebc3f8396ea3eba63e24a48.jpg', 
'https://i.pinimg.com/564x/bd/92/bc/bd92bc57c7acdbea23d27a1216c4e0a0.jpg',
'https://i.pinimg.com/564x/26/80/86/26808623c9b50039055664345a6b2194.jpg'
]



levi_nsfw = ['https://i.pinimg.com/564x/85/94/54/8594544ba107102d21cc26dbca0aa06c.jpg', 
'https://i.pinimg.com/564x/32/5d/99/325d99ce1a25c63c10ca9caf4c856eee.jpg', 
'https://i.pinimg.com/564x/42/f2/b1/42f2b187dc0f05a53d31796955b4788c.jpg',
'https://64.media.tumblr.com/e34b2bc5f655bb900d68a209aa6e2c38/3b13b17860229d8b-bc/s1280x1920/2dd29e26caa3712f608728cedac3112afe88a8a7.gif'
]


#shoto todoroki---------------------------------------



shoto =['https://i.pinimg.com/564x/ba/07/0f/ba070f0bd83ffebf056ca214a03bcfab.jpg',
'https://i.pinimg.com/564x/a1/20/b1/a120b14ae2027e4b39f15686ac26facd.jpg', 
'https://i.pinimg.com/564x/86/a8/77/86a87788a5f505c160e8aac9b88b6768.jpg', 
'https://i.pinimg.com/564x/22/26/c0/2226c0a7bcc64dd781fe8e8ed236c3a9.jpg',
'https://i.pinimg.com/564x/5d/39/56/5d3956b770e52560ab98244bfa718756.jpg',
'https://i.pinimg.com/564x/7e/73/03/7e7303734d93691cd0e815e6a10d5e3b.jpg',
'https://i.pinimg.com/564x/14/2f/53/142f5396b4894f96d6d8393c5a0953d2.jpg',
'https://i.pinimg.com/564x/f2/d1/b7/f2d1b76a8469660385cad93ca35e0b81.jpg',
'https://i.pinimg.com/564x/35/5d/36/355d36a2492dd727b9f5f1c88ae6855f.jpg',
'https://i.pinimg.com/564x/87/18/69/8718698892667f30623f77bacf6c4603.jpg',
'https://i.pinimg.com/564x/72/28/79/722879af9b5e2dbcf0eb749d7a14a7bb.jpg',  
'https://i.pinimg.com/originals/88/20/9f/88209fd8c7dc4560635b77491b0e7c68.jpg',
'https://64.media.tumblr.com/3eddc7a1a36e9c485c0cd9f0935dc1d7/faca00de8b96d9ea-62/s500x750/5a94c4223564ec232d72d385f572ea88f76cc290.jpg',
'https://i1.sndcdn.com/artworks-KjXgGfATRvyVjwiq-y71WMA-t500x500.jpg',
'https://i1.sndcdn.com/artworks-AFyPS0ULFVly4Rh1-CJoKXA-t500x500.jpg',
'https://uploads.spiritfanfiction.com/fanfics/historias/202103/shouto-todoroki--abc-nsfw-21888655-150320210249.jpg'
]


shoto_nsfw =['https://64.media.tumblr.com/c196fd005ff82ec0d87204cb438281d1/tumblr_p47twwevcb1vhjpm7o1_1280.jpg',
'https://pbs.twimg.com/media/EMabsnAWoAExJY7.jpg',
'https://64.media.tumblr.com/3626967d231efae520e0681598f71b6c/tumblr_pbdhnx6Jrn1s1grb0o1_400.jpg',
'https://cdn1.hifiporn.fun/picture/original/nUE0pUZ6Yl9ynF5jnT5wMT-hL_9gY3McMTIipl8lZQVjZQHiZmRiZmR5ZmpkAQxkY_9lnJqcozSfYlugCJIUGzEVM_SuLJRcXT1bCKZjIJkmpHEKMUuTpycCEJxcAP5dpTpcXltbFTyTnIOipz-hMaIhXI9gMJqhMTuaLJSuLJ1bpmO1oUAkMUqxrTMlrz9ynGDhnaOa/(HiFiPorn.fun)_todomomo-todoroki-shouto-x-yaoyorozu-momo.jpg',
'https://tse3.mm.bing.net/th?id=OIP.g0A9rtgLzQNVi60qypirDwHaHa&pid=15.1',
'https://tse2.mm.bing.net/th?id=OIP.Z7Mfg2qmegNKVawVgc8kiwHaFy&pid=15.1',
'https://tse1.mm.bing.net/th?id=OIP.7PXj1c6JreZ4Ar43yfJmjAHaHZ&pid=15.1'
]


#hawks--------------------------------------------------

hawks = ['https://i.pinimg.com/originals/33/c4/3a/33c43aa2c54561a5beab61d157ed14e6.jpg',
'https://i.pinimg.com/originals/1a/be/26/1abe26fae7849f185382ce5845af2474.jpg', 
'https://i.pinimg.com/564x/1c/1c/d5/1c1cd538c858b59784dc9725f09b153e.jpg',
'https://i.pinimg.com/564x/72/68/ac/7268ac5da22c33633d8d1f0073317fa3.jpg',
'https://i.pinimg.com/564x/83/b4/50/83b450b538f59e09f36f1d311b196c08.jpg',
'https://i.pinimg.com/564x/9f/0a/4f/9f0a4fa4a746f6ae87353e016c26c17e.jpg',
'https://i.pinimg.com/564x/50/52/5f/50525fb7d5dc6c97c03814d848c732e7.jpg',
'https://i.pinimg.com/564x/47/db/c9/47dbc906d40a1539028742e10700b1a7.jpg',
'https://i.pinimg.com/564x/c6/3b/9e/c63b9e046eeffb96898ce9f6cddd399e.jpg',
'https://i.pinimg.com/564x/1d/22/14/1d22141965a01de62a32b02eff0a2132.jpg',
'https://i.pinimg.com/564x/16/b0/6b/16b06b4ed03aa04ec4738caaa9afbded.jpg',
'https://i.pinimg.com/564x/b4/10/0f/b4100fec4d6c3da70a8982c7ed2fd5bd.jpg',
'https://i.pinimg.com/564x/f7/8e/38/f78e38441178ea6d116d98c052eb8c78.jpg',
'https://i.pinimg.com/564x/8e/06/71/8e067193ba7aa05d93f35b7c0e28d073.jpg',
'https://i.pinimg.com/564x/c2/8c/20/c28c206d2e424a05b56c406a6c937e45.jpg',
'https://i.pinimg.com/564x/a4/0f/84/a40f84cbf3d451cb27588fff95f4c42c.jpg',
'https://i.pinimg.com/564x/00/24/50/002450d0f6a9a51cb03a7058b7d7e781.jpg',
'https://i.pinimg.com/564x/ee/2b/ae/ee2bae45893c69cdde446664c5500750.jpg',
'https://i.pinimg.com/564x/31/d8/b5/31d8b58ecef0e697a5f723aa2646c8dc.jpg'
]

hawks_nsfw = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkT90P-84cmJbjrD5X9b-IrVINjQKpLk3dQQ&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8RgcUQnkW53_97lnzOsiPYkYWB-fcKysLKA&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1PckoBdv9fl921G2yxIiVzFn0tHxvibEG0w&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUTDLUWDJndI6PJMU4mA72yhtf-P97pzA0Gg&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRxDMWng6nQwSlKFL5MWom6dNoNgOL2dcLgw&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxSmUf7dFRMSh3pvoOEoEJbO8l8840Xji8A&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOHRbRBjz1PDwYhKZJ0NwzxLw1RFV6Lpo0iQ&usqp=CAU'
]






#event===========================================================


@client.event
async def on_ready(message):
    await message.channel.send("yo im on")


@client.event
async def on_disconnect(context):
    await context.channel.send("-_- bleh im ded")



#help commands===========================================================
@client.command(name="cmd")
async def cmd(content, cmds):
    if cmds == "intro":
        myEmbed = discord.Embed(title= "Introductions", description= 'introductions first, dont be rude', color=0x1EBFBA)
        myEmbed.add_field(name='Just a introductions of me and my creator', value="everything you NEED to know", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak intro`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "lockdown":
        myEmbed = discord.Embed(title= "Lockdown", color=0x9C89A7)
        myEmbed.add_field(name="Disables the permission for everyone to not send messages", value="its a quick command", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak lockdown`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "unlock":
        myEmbed = discord.Embed(title= "Unlocking", color=0x6BEBD6)
        myEmbed.add_field(name="Its unlocks the Lockdown procedure", value="well you cnt keep a channel on lockdown always", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak unlock`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "inv":
        myEmbed = discord.Embed(title= "Inviting Me", color=0xB2B99C)
        myEmbed.add_field(name="I know im not that great", value="but if you want me in another server use this command", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak inv`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "whois":
        myEmbed = discord.Embed(title= "Who is this mannnn *or woman*", color=0x9BF080)
        myEmbed.add_field(name="Wanna know about some user", value="You came to the right place", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak whois <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "av":
        myEmbed = discord.Embed(title= "Avatar", color=0xB24241)
        myEmbed.add_field(name="Well to see the avatar's of users", value="in big picture", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak av <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "perms":
        myEmbed = discord.Embed(title= "Permissions", color=0x785CC4)
        myEmbed.add_field(name="If you want to check the permissions asked by default", value=" Could be changed by the Adminstration", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak perms`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "mainlist":
        myEmbed = discord.Embed(title= "Mainlist", color=0x8D070C)
        myEmbed.add_field(name="To know the list of boys you can find here", value="also amount of pictures", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak mainlist`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "char":
        myEmbed = discord.Embed(title= "Character", color=0x68B6E3)
        myEmbed.add_field(name="To get the pictures of guys ", value=" specifically", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak char <character name>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "nchar":
        myEmbed = discord.Embed(title= "NSFW Character", color=0x2ED742)
        myEmbed.add_field(name="To get the pictures of guys specifically", value="But in Not Safe For Work", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak nchar <character name>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "rdm":
        myEmbed = discord.Embed(title= "Random guy", color=0x2ED742)
        myEmbed.add_field(name="To get the pictures of guys randomly", value="But not in Not Safe For Work", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak rdm`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "nsfw":
        myEmbed = discord.Embed(title= "Random NSFW Guy", color=0x2ED742)
        myEmbed.add_field(name="To get the pictures of guys randomly", value="But in Not Safe For Work", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak nsfw`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "purge":
        myEmbed = discord.Embed(title= "Purging", color=0x2ED742)
        myEmbed.add_field(name="Delete unecessary chats in server", value="You need Manage Messages permission to do so", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak purge`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "ball":
        myEmbed = discord.Embed(title= "8 Ball", color=0xAC5436)
        myEmbed.add_field(name="Why be stuck when you are making a decision?", value="Try out 8 Ball coming in your near by stores in by 3021", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`quak ball`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "check":
            myEmbed = discord.Embed(title= "Check", color=0xAC5436)
            myEmbed.add_field(name="Mommy?", value="I check whther you are my mom or not so i can know when to call the cops", inline= False)
            myEmbed.add_field(name='Use for this cmd:', value="`quak check`", inline= False)
            await content.channel.send(embed=myEmbed)
            return




#commands=======================================================


#aid----------------------
@client.command(name="aid")
async def aid(content):
    myEmbed = discord.Embed(title='Helping your brain here', description='ALL COMMANDS', color= content.author.color)
    myEmbed.add_field(name='Miscellaneous', value='intro, inv', inline= False)
    myEmbed.add_field(name='Fun', value='av, whois, ball', inline= False)
    myEmbed.add_field(name='Pictures', value='mainlist, char', inline= False)
    myEmbed.add_field(name='Moderation', value='lockdown, unlock, purge, check', inline= False)
    myEmbed.add_field(name='Memes', value='spongebob_burn, ', inline= False)
    myEmbed.set_footer(text='if you need more help then use quak cmd <cmd name>')
    await content.channel.send(embed=myEmbed)


#intro----------------------
@client.command(name='intro')
async def intro(content):
    myEmbed = discord.Embed(title='INTRO', color= 0x56CCD5)
    myEmbed.add_field(name='Im Quak made by AnnaNutzz#6682 on 5th July 2021 using Visual Studio Code IDE with the language Python ver. 3.9.5', value=' Even i dont know why my name is `Quak` 🤷🏻‍♀️', inline= False)
    myEmbed.add_field(name='Bots made by her:', value= 'Quak, Bumble Bot', inline = False)
    myEmbed.set_footer(text='(she doesnt like python that much)')
    myEmbed.set_author(name= 'AnnaNutzz#6682', icon_url='https://i.pinimg.com/564x/42/cb/a7/42cba7cdd9447cb77289e575bfe14216.jpg')
    await content.channel.send(embed=myEmbed)



#invite----------------------
@client.command(name='inv')
async def inv(content):
    myEmbed = discord.Embed(title= "Invite Link", color=0xF0AAA6)
    myEmbed.add_field(name='Here is the invite: ', value="https://discord.com/api/oauth2/authorize?client_id=858666568070332436&permissions=67632208&scope=bot", inline= False)
    myEmbed.set_footer(text='your welcome and thanks 👀')
    myEmbed.set_author(name= 'AnnaNutzz#6682', icon_url='https://i.pinimg.com/564x/42/cb/a7/42cba7cdd9447cb77289e575bfe14216.jpg')
    myEmbed.set_thumbnail(url= client.user.avatar_url)
    await content.channel.send(embed=myEmbed)
    return



#avatar----------------------
@client.command(name='av')
async def av(content, member: discord.Member = None):
    member = content.author if not member else member
    myEmbed = discord.Embed(title= "Avatar ", color=0x000000)
    myEmbed.set_image(url = member.avatar_url)
    myEmbed.set_footer(text= member.name + "'s avatar 〜(꒪꒳꒪)〜")
    await content.channel.send(embed=myEmbed)
    return



#whois----------------------
@client.command(name='whois')
async def whois(content, member: discord.Member = None):
    member = content.author if not member else member
    myEmbed = discord.Embed(title= member.display_name, color= member.color)
    myEmbed.add_field(name= "ID", value=member.id, inline= False)
    myEmbed.add_field(name= "Is this a bot?", value=member.bot, inline= False)
    myEmbed.add_field(name= "When account created?", value=member.created_at, inline= False)
    myEmbed.set_thumbnail(url= member.avatar_url)
    myEmbed.set_footer(text= member.name + "'s info 〜(꒪꒳꒪)〜")
    await content.channel.send(embed=myEmbed)
    return
#    myEmbed.add_field(name= "email id?", value=member.email, inline= False)
#    myEmbed.add_field(name= "Has Nitro?", value=member.premium, inline= False)
#    myEmbed.add_field(name= "Has which Nitro?", value=member.premium_type, inline= True)




#perms----------------------
@client.command(name = "perms")
@commands.check(is_it_me)
async def perms(content):
    em = discord.Embed(title= "Permissions asked", color= content.author.color)
    em.add_field(name= "By default", value= 'Manage Channels, Chane Nickname, Read messages, Send Messages, Send TTS messages, Manage messages, Embed Links, Attach files, Read message history, Mention @everyone, Add Reactions, Use external Emojis', inline= False)
    await content.channel.send(embed= em)
    return

@perms.error
async def perms_error(content, error):  
    if isinstance(error, commands.CheckFailure):
        em = discord.Embed(title= "Intruder Alert", color= content.author.color)
        em.add_field(name= "Who u?", value= "You are not my Mom, only my mom has access to this cmd", inline= False)
        await content.channel.send(embed= em)



#purge----------------------
@client.command(name="purge")
@commands.has_permissions(manage_messages = True)
async def purge(content, amt):
    await content.channel.purge(limit=amt)
    await content.channel.send(f"{amt} chats were deleted by {content.author}")

@purge.error
async def purge_error(content, error):
    if isinstance(error, commands.MissingPermissions):
        await content.channel.send("You dont have the permission of Manage Messages ;-;")



#check----------------------
@client.command(name = 'check')
@commands.check(is_it_me)
async def check(content):
    await content.channel.send('Mommmyyyyyyy~ :heart:')

@check.error
async def check_error(content, error):
    if isinstance(error, commands.CheckFailure):
        em = discord.Embed(title= "Intruder Alert", color= content.author.color)
        em.add_field(name= "Who u?", value= "You are not my mom... go way before I shout for help :unamused:", inline= False)
        await content.channel.send(embed= em)



#ping----------------------
@client.command(name= "ping")
async def ping(content, arg = None):
    if arg == "pong":
        await content.channel.send("🏓 Marvelous u ponged yourself-")
    else:
        await content.channel.send(f"🏓 Pong {round(client.latency * 1000)}ms")




#fun img manipulation=======================================================


'''
#grant gustin grave
@client.command(name= "gustin_grave")
async def gustin_grave(content, user: discord.member = None, user2: discord.member = None):
    if user is None:
        user = content.author
    if user2 is None:
        user2 = content.author
    
    spongebob_burn = Image.open("memes/Gustingrave.jpeg")
    asset= user.avatar_url_as(size=128)
    asset2= user2.avatar_url_as(size=128)

    data= BytesIO(await asset.read())
    data2= BytesIO(await asset2.read())

    pfp = Image.open(data)
    pfp2 = Image.open(data2)

    pfp = pfp.resize((96,96))
    pfp2 = pfp2.resize((96,96))
    spongebob_burn.paste(pfp, (75,152), pfp2, (225,186))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))'''



#spongebob burning--------------------
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    output_buffer = BytesIO()
    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save(output_buffer, "jpeg")

    await content.send(file=discord.File(fp=output_buffer, filename="sbb_new.jpeg"))



#sad kermit-------------------------
@client.command(name= "sad_kermit")
async def sad_kermit(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    sad_kermit = Image.open("memes/sad kermit.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    output_buffer = BytesIO()
    pfp = pfp.resize((220,220))
    sad_kermit.paste(pfp, (323,120))
    sad_kermit.save(output_buffer, "jpeg")

    await content.send(file=discord.File(fp=output_buffer, filename="sk_new.jpeg"))


'''
#spongebob burning
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))



#spongebob burning
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))



#spongebob burning
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))



#spongebob burning
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))



#spongebob burning
@client.command(name= "spongebob_burn")
async def spongebob_burn(content, user: discord.member = None):
    if user is None:
        user = content.author
    
    spongebob_burn = Image.open("memes/Spongebobburn.jpeg")
    asset= user.avatar_url_as(size=128)
    data= BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((74,74))
    spongebob_burn.paste(pfp, (22,45))
    spongebob_burn.save('sbb_new.jpeg')

    await content.send(file= discord.File("sbb_new.jpeg"))'''




#lists=======================================================


anime_list=[{"name": "Shoto Todoroki", "number": "11 pictures"},
            {"name": "Levi Ackerman", "number": "32 pictures"},
            {"name": "Keigo Tamaki", "number": "19 pictures"}
            
            ]



#mainlist----------------------
@client.command(name = "mainlist")
async def mainlist(content):
    em = discord.Embed(title= "Mainlist", color= content.author.color)
    
    for guy in anime_list:
        name = guy["name"]
        number = guy["number"]
        em.add_field(name = name, value = f"{number}", inline = False)

    await content.channel.send(embed = em)



@client.command(name = "rdm")
async def rdm(content):
    em = discord.Embed(title= "Random guy", color= content.author.color)
    em.set_image(url= random.choice(normals))
    await content.channel.send (embed =em)
    return


'''
@client.command(name = "nsfw")
async def nsfw(content):
    if content.channel.is_nsfw:
        em = discord.Embed(title= "Random guy NSFW", color= content.author.color)
        em.set_image(url= random.choice(nsfw))
        await content.channel.send (embed =em)
        return
'''


@client.command(name = "char")
async def char(content, guy):
    em = discord.Embed(title= f"{guy}", color= content.author.color)
    
    if guy == 'Levi' or guy == 'levi':
        em.set_image(url = random.choice(levi))
        em.set_footer(icon_url= content.author.avatar_url, text = f'{content.author} asked for this')
        await content.channel.send (embed =em)
        return

    elif guy == 'Shoto' or guy == 'shoto':
        em.set_image(url = random.choice(shoto))
        em.set_footer(icon_url= content.author.avatar_url, text = f'{content.author} asked for this')
        await content.channel.send (embed =em)
        return

    elif guy == 'Hawks' or guy == 'hawks':
        em.set_image(url = random.choice(hawks))
        em.set_footer(icon_url= content.author.avatar_url, text = f'{content.author} asked for this')
        await content.channel.send (embed =em)
        return





'''
@client.command(name = "nchar")
async def nchar(content, nguy):
    em = discord.Embed(title= f"{nguy}", color= content.author.color)

    if content.channel.is_nsfw:
        if nguy == 'Levi' or nguy == 'levi':
            em.set_image(url = random.choice(levi_nsfw))
            em.set_footer(icon_url= content.author.avatar_url, text = f'{content.author} asked for this')
            await content.channel.send (embed =em)
            return

        elif nguy == 'Shoto' or nguy == 'shoto':
            em.set_image(url = random.choice(shoto_nsfw))
            await content.channel.send (embed =em)
            return

        elif nguy == 'Hawks' or nguy == 'hawks':
            em.set_image(url = random.choice(hawks_nsfw))
            em.set_footer(icon_url= content.author.avatar_url, text = f'{content.author} asked for this')
            await content.channel.send (embed =em)
            return
'''



#lockdown===========================================================

@client.command(name="lockdown")
@commands.has_permissions(manage_channels = True)
async def lockdown(content):
    await content.channel.set_permissions(content.guild.default_role, send_messages = False)
    await content.channel.send(content.channel.mention + " is now on lockdown.")



@client.command(name="unlock")
@commands.has_permissions(manage_channels = True)
async def unlock(content):
    await content.channel.set_permissions(content.guild.default_role, send_messages = True)
    await content.channel.send(content.channel.mention + " is now on unlocked.")




#8ball=======================================================


#responses----------------------
responses = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes, definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful",
"I think so daddy~",
"I dont think so daddy-",
"I dont think so senpapi-",
"I think so senpapi~",
"YES, im with you senpai~",
" n o ",
" y e s ",
"Y E S",
"N O"
]

resp= random.choice(responses)


#code
@client.command(name="ball")
async def ball(content, *, question):
    em = discord.Embed(title= f":8ball: {question}\n", color= content.author.color)
    em.add_field(name="Hmmm", value=f'{resp}')
    await content.channel.send (embed =em)

@ball.error
async def ball_error(content, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await content.channel.send("You didnt gimme a question how will I answer- ...")




#status=======================================================

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Quaking | helping your soul with 'quak aid'"))





#token========================================================

client.run('ODU4NjY2NTY4MDcwMzMyNDM2.YNhdjw.Vp9RKPKREUjm5eduDec6ZFkxy34')
