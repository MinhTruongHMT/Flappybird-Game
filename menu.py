import pygame,sys,json
from random import randint
pygame.init()
screen = pygame.display.set_mode((400,600))
clock= pygame.time.Clock()
#_______________tao_phong_chu____________________________________________________________
game_font =pygame.font.Font('04B_19.ttf',40)
font2=pygame.font.SysFont("verdana",40)
font3 =pygame.font.Font('04B_19.ttf',25)
#______________tao_anh_vao_chuong_trinh__________________________________________________
background_img = pygame.image.load('images/background-night.png').convert_alpha()
background_img = pygame.transform.scale(background_img,(400,600))
background = pygame.image.load('images/background1.png').convert_alpha()
background= pygame.transform.scale(background,(400,600))
backgroundchieu = pygame.image.load('images/backgroundchieu.png').convert_alpha()
backgroundchieu= pygame.transform.scale(backgroundchieu,(620,650))
toptable= pygame.image.load('images/toptable.jpg').convert_alpha()
toptable=pygame.transform.scale(toptable,(400,600))
floor_img = pygame.transform.scale2x(pygame.image.load('images/floor.png').convert_alpha())
play_img=pygame.image.load('images/play.png')
top_img=pygame.image.load('images/top.png')
exit_img=pygame.image.load('images/exit.png')
tube_img=pygame.image.load('images/tube.png').convert_alpha()
tubeop_img=pygame.image.load('images/tube_op.png').convert_alpha()
chimMid=pygame.image.load('images/bird1.png').convert_alpha()
chimDown=pygame.image.load('images/bird2.png').convert_alpha()
chimUp=pygame.image.load('images/bird3.png').convert_alpha()
ketthuc = pygame.image.load('images/ketthuc.png').convert_alpha()
ketthuc = pygame.transform.scale(ketthuc,(400,600))
#__________________am_thanh______________________________________________________________
pygame.mixer.music.load('sound/nhac.ogg')
flay_sound =pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound =pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound =pygame.mixer.Sound('sound/sfx_point.wav')

#__________________button_________________________________________________________________
class Button():
	def __init__(self,x,y,image):
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.topleft =(x,y)
		self.clicked =False
	def draw(self):
		action =False
		pos = pygame.mouse.get_pos()
	
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]==1 and self.clicked ==False:
				self.clicked=True
				action=True
		if pygame.mouse.get_pressed()[0]==0:
			self.clicked=False
		screen.blit(self.image,(self.rect.x,self.rect.y))
		return action
#_______________________khai_bao_bien_________________________________________________

#__________danh_sach_thon_tin_nguoi_choi________________________________________
dic={}
#__________doc_file_______________________________________________________________________
with open('game.txt') as test_file:
	dic=json.load(test_file)
tube_width=60 
tube_height=400
tube1_y=randint(400,500)
tube2_y=randint(400,500)
tube3_y=randint(400,500)
newname=''
birdFlap=pygame.USEREVENT
pygame.time.set_timer(birdFlap,200)
#_______________________ham_xu_ly_them________________________________________________
def taottnguoiChoi(name):
	dic[name]=0
def kiemTraMaNguoiChoi(list,key):
	for i in dic.keys():
		if(i==key):
			return True
	return False
#_______________________game___________________________________________________________
def game():
	birdList=[chimDown,chimMid,chimUp]
	pygame.mixer.music.load('sound/nhac.ogg')
	pygame.mixer.music.play(-1)#am thanh nen cua game
	running =True
	floor_x=0
	bird_x=50
	bird_y=350
	bird_drop_velocity=0
	gravity =0.5
	birdIndex=0 
	bird1=birdList[birdIndex]
	tube1_x=400
	tube2_x=700
	tube3_x=1000
	score = 0
	highscore=0
	endscore=0
	tube1_pass=False
	tube2_pass=False
	tube3_pass=False
	tube_velocity=2
	aa=0
	game_end= False
	pausing = False
	game_run= True
	def draw_floor():
		screen.blit(floor_img,(floor_x,550))
		screen.blit(floor_img,(floor_x+432,550))
	def doichim():
		newBird=birdList[birdIndex]
		return newBird
	while running:
		clock.tick(80)
		highscore_txt= font3.render('Best Score :'+str(highscore),True,(0,0,0))
		end_score=font3.render('End Score  :'+str(endscore),True,(0,0,0))
		#backgound
#________________anh_nen_cua_game________
		if aa<3:
			screen.blit(background_img,(0,0))
		elif aa<7:
			screen.blit(backgroundchieu,(0,0))
		elif aa<15:
			screen.blit(background,(0,0))
		else:
			aa=0
		if game_run:
#_______________chim___________________
			#ve chim
			bird1=doichim()
			bird=screen.blit(bird1,(bird_x,bird_y))
			#chim roi
			bird_y+=bird_drop_velocity
			bird_drop_velocity+=gravity
#________________ong___________________
#-----ve_ong_tren_______________________
			tube1_img = pygame.transform.scale(tube_img,(tube_width,tube_height))
			tube1=screen.blit(tube1_img,(tube1_x,(-1*(600-tube1_y))))
			tube2_img = pygame.transform.scale(tube_img,(tube_width,tube_height))
			tube2=screen.blit(tube2_img,(tube2_x,(-1*(600-tube2_y))))
			tube3_img = pygame.transform.scale(tube_img,(tube_width,tube_height))
			tube3=screen.blit(tube3_img,(tube3_x,(-1*(600-tube3_y))))
			#-----ve_ong_duoi
			tubeop1_img = pygame.transform.scale(tubeop_img,(tube_width,tube_height))
			tube1op=screen.blit(tubeop1_img,(tube1_x,tube1_y))
			tubeop2_img = pygame.transform.scale(tubeop_img,(tube_width,tube_height))
			tube2op=screen.blit(tubeop2_img,(tube2_x,tube2_y))
			tubeop3_img = pygame.transform.scale(tubeop_img,(tube_width,tube_height))
			tube3op=screen.blit(tubeop3_img,(tube3_x,tube3_y))
#-----di_chuyen_ong
			tube1_x-=tube_velocity
			tube2_x-=tube_velocity
			tube3_x-=tube_velocity
#------tao_ong_moi
			if tube1_x<-60:
				tube1_x=840
				tube1_pass=False
			if tube2_x<-60:
				tube2_x=840
				tube2_pass=False
			if tube3_x<-60:
				tube3_x=840
				tube3_pass=False
#_______________ve_nen dat________________
			floor_x-=2
			draw_floor()
			#di chuyển đất
			if floor_x<-432:
				floor_x=0
#________________diem____________________
		#----------------hien_thi_diem-----------
			score_txt= game_font.render(str(score),True,(255,255,255))
			screen.blit(score_txt,(200,120 ))
#----------------tinh_diem----------------
			if tube1_x+tube_width<bird_x and tube1_pass==False:
				score+=1
				aa+=1
				score_sound.play()
				tube1_pass=True
			if tube2_x+tube_width<bird_x and tube2_pass==False:
				score+=1
				aa+=1
				score_sound.play()
				tube2_pass=True
			if tube3_x+tube_width<bird_x and tube3_pass==False:
				score+=1
				aa+=1
				score_sound.play()
				tube3_pass=True
#________________xu_ly_qua_cham_________________
			tubes=[tube1,tube2,tube3,tube1op,tube2op,tube3op]
			for tube in tubes:
				if bird.colliderect(tube):
					pygame.mixer.pause();
					hit_sound.play();
					tube_velocity=0
					bird_drop_velocity=0
					pausing=True
					game_run=False;
					game_end=True;
			if bird_y<-70 or bird_y>500:
					pygame.mixer.pause();
					hit_sound.play();
					tube_velocity=0
					bird_drop_velocity=0
					pausing =True
					game_run=False;
					game_end=True;
#______________mang_hinh_end_game____________
		if game_end:
			#vẽ đất
			floor_x-=2
			draw_floor()
			#di chuyển đất
			if floor_x<-432:
				floor_x=0
			screen.blit(ketthuc,(0,0))
			
			if score>highscore:
				highscore=score
			endscore=score
			screen.blit(highscore_txt,(150,350))
			screen.blit(end_score,(150,300))
			# screen.blit(score_txt,(187,0 ))
			if kiemTraMaNguoiChoi(dic,newname)==True:
				if dic[newname]<score:
					dic[newname]=score
			else:
				taottnguoiChoi(newname)
				if dic[newname]<score:
					dic[newname]=score
#__________bat_su_kien_nguoi_choi_____________
		for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							with open('game.txt','w') as test_file:
								json.dump(dic,test_file)
							running=False
						if event.key ==pygame.K_SPACE:
							bird_drop_velocity=0
							bird_drop_velocity-=8
							flay_sound.play()
							if pausing:
								pausing=False
								game_run=True;
								game_end=False;
								tube1_x=400
								tube2_x=700
								tube3_x=1000
								bird_x=50
								bird_y=350
								tube_velocity=2
								score = 0
								floor_x-=2
								aa=0
								endscore=score
					if event.type==pygame.MOUSEBUTTONDOWN:
						bird_drop_velocity=0
						bird_drop_velocity-=8
						flay_sound.play()
						if pausing:
							pausing=False
							game_run=True;
							game_end=False;
							tube1_x=400
							tube2_x=700
							tube3_x=1000
							bird_x=50
							bird_y=350
							tube_velocity=2
							score = 0
							floor_x-=2
							aa=0
							endscore=score
					if event.type==birdFlap:
						if birdIndex<2:
							birdIndex+=1
						else:
							birdIndex=0

		pygame.display.flip()
		pygame.display.update()
	pygame.mixer.music.load('sound/music.mp3')
	pygame.mixer.music.play(-1)#am thanh nen cua game
#______________________nhap_name_________________________________________________________
def nhapname():
	running =True
	global newname
	name=''
	def draw (screen,font,text,color,x,y):
		text =font.render(text,True,color)
		screen.blit(text,(x,y))
	def box_input(screen,x,y,width,height):
		pygame.draw.rect(screen,(255,255,255),(x,y,width,height))
	while running:
		clock.tick(80)
		screen.blit(background_img,(0,0))
		draw(screen,game_font,'NAME',((255,255,255)),150,100)
		box_input(screen,60,200,307,75)
		# choi=game_font.render('TOP',True,(255,255,255))
		# choi_rect = choi.get_rect(center=(200,155))
		# screen.blit(choi,choi_rect)
		
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						newname=name
						# running=False
					elif len(name)<8 and event.key!=pygame.K_BACKSPACE and event.key!=pygame.K_RETURN and event.key !=pygame.K_SPACE:
						name+=event.unicode
					elif event.key==pygame.K_BACKSPACE:
							name=name[:-1]
					elif event.key==pygame.K_RETURN:
						newname=name
						running=False
		draw(screen,font2,name,((0,0,0)),80,215)
		pygame.display.flip()


#______________________chuong_trinh_chinh________________________________________________
def main_menu():
	play_button = Button(145,100,play_img)
	top_button = Button(150,200,top_img)
	exit_button = Button(140,300,exit_img)
	while True:
		screen.blit(background_img,(0,0))
		if play_button.draw() == True:
			nhapname() 
			if newname!='':
				game()
		if top_button.draw() ==True:
			top()#goi hien thi top 3 player
		if exit_button.draw() ==True:
			pygame.quit()#ket thuc khi nhan ESC
			sys.exit();	
		clock.tick(80)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				with open('game.txt','w') as test_file:
					json.dump(dic,test_file)
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					with open('game.txt','w') as test_file:
						json.dump(dic,test_file)
					pygame.quit()
					sys.exit();		
		pygame.display.flip()
		pygame.display.update()
pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1)#am thanh nen cua game
#_______________________(hien_thi_DS_PLAYER)_______________________________________________
def top():
	running =True
	def ve():
		y=230
		dic2=sorted(dic.values(), reverse=True)
		dic2=set(dic2)
		dic3=sorted(dic2, reverse=True)
		soluong=0
		for i in range(len(dic3)):
			for n in dic:
				if dic[n]==dic3[i] and soluong<5:
					scoretop1= game_font.render(f'{dic[n]}',True,(0,0,0))
					screen.blit(scoretop1,(266,y ))
					scoretop6= game_font.render(f'{n}',True,(0,0,0))
					screen.blit(scoretop6,(83,y ))
					y+=40
					soluong+=1
	# choi=game_font.render('TOP',True,(255,255,255))
	screen.blit(toptable,(0,0))
	ve()
	while running:
		clock.tick(80)
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running=False
		pygame.display.flip()
		pygame.display.update()
main_menu()

