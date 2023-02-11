prev_distance = 0
reward=0
step=0
def game(weight,generation):
    import pygame
    import time,math
    import random
    import tensorflow as tf
    import tensorflow.keras
    import keras
    import numpy as np
    pygame.init()
     
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
     
    dis_width = 600
    dis_height = 400
     
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')
     
    clock = pygame.time.Clock()
     
    snake_block = 10
    snake_speed = 100
     
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    # input_layer = tf.keras.layers.Input(shape=(6,))

    # hidden_layer_1 = tf.keras.layers.Dense(8, activation='relu')(input_layer)

    # output_layer = tf.keras.layers.Dense(3, activation='softmax')(hidden_layer_1)

    # model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)


    def distance(snake_head, food_location):
        x1, y1 = snake_head
        x2, y2 = food_location
        print(((x2 - x1)**2 + (y2 - y1)**2)**0.5)

     
    def Your_score(score):
        value = score_font.render("Generation : " + str(score), True, yellow)
        dis.blit(value, [0, 0])
     
     
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    
     
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
     

    def calculate_reward(snake_x, snake_y, food_x, food_y):
        global prev_distance
        global reward
        current_distance = ((snake_x - food_x) ** 2 + (snake_y - food_y) ** 2) ** 0.5
        if current_distance < prev_distance:
            reward += 1
        else:
            reward -= 1
        prev_distance = current_distance
        return reward
        

    def gameLoop(weight):
        global reward
        global step
        game_over = False
        game_close = False
        input_layer = tf.keras.layers.Input(shape=(6,))
        hidden_layer_1 = tf.keras.layers.Dense(12, activation='relu')(input_layer)
        hidden_layer_2 = tf.keras.layers.Dense(16, activation='relu')(hidden_layer_1)
        hidden_layer_3 = tf.keras.layers.Dense(8, activation='relu')(hidden_layer_2)
        output_layer = tf.keras.layers.Dense(4, activation='softmax')(hidden_layer_3)
        model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)
            
        model.set_weights(weight)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
      
        x1 = dis_width / 2
        y1 = dis_height / 2
     
        x1_change = 0
        y1_change = 0
     
        snake_List = []
        Length_of_snake = 1
     
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
     
        while not game_over:

            p1=1
            p2=1
            p3=1
            p4=1
            p5=1
            p6=1
            p7=0
     
            while game_close == True:
                time.sleep(.1)
                # print('\n\n value send\n\n')
                # create a file named "rewards_weights.txt" in write mode
                # with open("rewards_weights.txt", "a") as f:
                #     # write the rewards and weights to the file
                #     f.write("Rewards: " + str(reward) + "\n")
                #     f.write("Weights: " + str(weight) + "\n")
                
                return_value= reward
                reward=0
                step=0
                return return_value, weight
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
     
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head :
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(generation)
            
            # distance(snake_Head,(foodx,foody))
            calculate_reward(x1,y1,foodx,foody)

      
            if [x1+20, y1] in snake_List:
                p1=0
            if [x1, y1+20]  in snake_List:
                p2=0
            if [x1-20, y1] in snake_List:
                p3=0
            if [x1, y1-20] in snake_List:
                p4=0
            if (x1+20) > 600 or (x1+20)<0:
                p1=0
            if y1+20 > 400 or y1+20<0:
                p2=0
            if (x1-20) > 600 or (x1-20)<0:
                p3=0
            if y1-20 > 400 or y1-20<0:
                p4=0

            p5=x1-foodx
            p6=y1-foody

            input_values = [[p1, p2, p3, p4, p5, p6]]
            prediction = model.predict(input_values, verbose=0)
            arr = np.array(prediction)
            index = np.argmax(arr)
            if index==0:
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
            if index==1:
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP))
            if index==2:
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
            if index==3:
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))

            step+=1
            if step == 1000:
                game_close = True
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
                reward=50

            # print(f'reward :  {reward}')
            clock.tick(snake_speed)
        pygame.quit()
        quit()
    
    
    return gameLoop(weight)
