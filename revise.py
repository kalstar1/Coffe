from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import base64, io, re
root=Path(__file__).resolve().parent
photo=root.parent/'uploads'/'20261006_201904-c43346b8-c447-4e33-aeca-19077d2cacd4.jpg'
im=Image.open(photo).convert('RGBA')
w,h=im.size
mask=Image.new('L',(w,h));d=ImageDraw.Draw(mask)
def pts(p): return [(int(x*w/1568),int(y*h/1477)) for x,y in p]
d.polygon(pts([(550,170),(560,127),(645,92),(820,65),(1080,59),(1330,83),(1450,124),(1525,176),(1533,258),(1492,770),(1456,1167),(1417,1264),(1290,1328),(1100,1358),(858,1337),(717,1282),(651,1187),(602,1030),(441,980),(262,903),(132,793),(67,649),(40,519),(69,442),(132,393),(239,373),(311,411),(373,454),(439,345),(510,293),(567,283)]),fill=255)
d.polygon(pts([(563,470),(515,425),(462,471),(419,536),(374,560),(316,542),(255,493),(184,458),(137,478),(126,533),(153,640),(205,736),(298,812),(407,856),(548,883),(590,879)]),fill=0)
mask=mask.filter(ImageFilter.GaussianBlur(1.1));im.putalpha(mask)
im=im.crop((int(30*w/1568),int(52*h/1477),int(1543*w/1568),int(1370*h/1477)))
im.thumbnail((700,700));buf=io.BytesIO();im.save(buf,format='PNG');data=base64.b64encode(buf.getvalue()).decode()
p=root/'index.html';html=p.read_text(encoding='utf8')
html=html.replace("type==='blue'?pink:","type==='blue'?'<img class=\"real-cup\" alt=\"Your pale blue cup with its original pink character artwork and heart-shaped handle\" src=\"data:image/png;base64,"+data+"\">':")
html=html.replace('Inspired by your real cup','Your actual cup · photo edition')
html=html.replace("const feelings=['a smile','thinking of you','a little mischief','your company','warmth','a softer day','a reason to smile','a little courage','being here','♡','choosing you','love, without guessing'];", "const feelings=['🐸','those eyes of yours','💎','the little details on your nails','🦋','that smile. yes, that one.','the way you make an outfit yours','a little swing, a little freedom','the way you notice who needs care','your heart makes room for people','how you keep seeing the good','the kindness you give so freely','your softness is not a small thing','a little mischief','you make ordinary days warmer','being here, with you','♡','love, without guessing'];")
html=html.replace("$('dropword').textContent=feelings[index];", "if(feelings[index]==='a little swing, a little freedom'){$('dropword').innerHTML='<svg class=\"swing-icon\" viewBox=\"0 0 80 80\" aria-label=\"A swing\" role=\"img\"><path d=\"M12 10H68M25 10V53M55 10V53\" fill=\"none\" stroke=\"#efd4a7\" stroke-width=\"3\"/><path d=\"M19 53Q40 63 61 53L59 60Q40 68 21 60Z\" fill=\"#d5a778\"/></svg><span>a little freedom</span>'}else{$('dropword').textContent=feelings[index]}")
css='''
/* Second visual study: photograph-faithful cup and cinematic staging. */
.room{background:radial-gradient(ellipse at 73% 16%,#dda66f26,transparent 42%),radial-gradient(ellipse at 50% 75%,#6977591f,transparent 65%),linear-gradient(110deg,#152b29,#232d25 55%,#101916)}
.room:after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse,transparent 35%,#050e1280);pointer-events:none}
.window{border-color:#273f38;background:linear-gradient(135deg,#79999655,#203f44 60%,#152b32);box-shadow:inset 0 0 70px #10252f,0 0 150px #9bbbab18}
main{position:relative}h1{text-shadow:0 5px 35px #0005}.eyebrow{color:#e1bb86}
.cups{position:relative;padding:25px 0 14px;margin-top:39px;gap:65px}
.cups:before{content:'';position:absolute;bottom:46px;left:8%;right:8%;height:60px;border-radius:50%;background:radial-gradient(ellipse,#bb966424,transparent 70%);filter:blur(8px)}
.choice{width:215px}.choice:before{content:'';position:absolute;width:180px;height:32px;border-radius:50%;background:radial-gradient(ellipse,#eee1bf55,#a6a89233 55%,transparent 72%);top:164px;left:18px;transform:rotateX(50deg)}
.choice .mug{animation:sway 9s ease-in-out infinite}.choice .blue{animation:photoFloat 8s ease-in-out infinite}
.mug.blue{background:none;box-shadow:none;width:190px;height:165px;border-radius:0;transform-style:flat}
.mug.blue:before,.mug.blue>.handle{display:none}.real-cup{position:absolute;inset:-14px -8px auto auto;width:190px;height:174px;object-fit:contain;filter:drop-shadow(8px 14px 9px #0006)}
.choice:hover .blue,.choice.selected .blue{animation:none;transform:translateY(-14px) scale(1.1)}
.choice.selected:after{bottom:-13px}.choice.selected .label{color:#f2d3a7}.label{margin-top:31px}.sub{color:#abb0a0;line-height:1.5}
.machine{background:linear-gradient(105deg,#344e43,#69806b 30%,#415d48 67%,#263e31);border-color:#859679;box-shadow:20px 30px 65px #0009,inset 2px 2px 4px #d3d8ad55,inset -5px 0 15px #152c2666}
.machine:after{content:'';position:absolute;left:12px;top:25px;bottom:35px;width:5px;border-radius:50%;background:linear-gradient(transparent,#b5c6a94d,transparent)}
.brew-scene:after{content:'';position:absolute;bottom:33px;left:10px;width:340px;height:32px;background:#080d0b88;border-radius:50%;filter:blur(16px);z-index:-1}
.brewing-cup:has(.blue){left:65px;top:262px;transform:scale(.84)}
.blue .liquid{left:70px;right:8px;top:-5px;height:14px;transform:rotate(-1deg)}.blue .steam{left:108px;top:-53px}
.dropword{left:-25px;right:-25px;font-size:clamp(18px,3vw,24px);line-height:1.35;top:182px;padding:0 15px;text-wrap:balance;filter:drop-shadow(0 3px 8px #000);pointer-events:none}
.swing-icon{display:block;width:50px;height:50px;margin:-22px auto 0}.swing-icon+span{font-size:16px}
.drop{background:radial-gradient(circle at 30% 25%,#fff7d8,#e5b365 40%,#8b4f28 85%);box-shadow:0 0 20px #f4bd7544,inset 1px 1px 2px #ffeacb}
.end{border-top:1px solid #b6a17b33;margin-top:10px;padding-top:32px}.end h2{font-size:38px}.counter{height:82px;background:repeating-linear-gradient(0deg,#8063430a 0 1px,transparent 2px 9px),linear-gradient(#5c4732,#2e251c)}
@keyframes photoFloat{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-7px) rotate(2deg)}}
@media(max-width:600px){.cups{gap:1px;padding-top:15px;margin-top:35px}.choice{width:33%}.choice:before{width:95px;height:20px;top:115px;left:0}.choice .mug{zoom:.58}.choice .blue{zoom:.55}.label{font-size:13px;margin-top:30px}.sub{font-size:8px;padding:0 3px}.dropword{font-size:20px}.end h2{font-size:31px}}
@media(prefers-reduced-motion:reduce){.choice .blue,.choice .mug{animation:none}}
'''
html=html.replace('</style>',css+'</style>')
html=html.replace('I hope being in your life feels like this:', 'You give so much warmth to other people.<br>I hope being in your life feels like this:')
p.write_text(html,encoding='utf8')
print('Revised self-contained website. Photo dimensions:',w,h,'; 18 personalized drops; swing illustration included.')
