import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


/**
 * Write a description of class player here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */


public class player extends Actor
{
    /**
     * Act - do whatever the player wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    
    int x,y;
    double fallSpeed = 0.1;
    double velocity = -2;
    int frameCount = 0;
    
    public void act() 
    {
        setLocation(x,y);
        frameCount++;
        if(Greenfoot.isKeyDown("space") && isTouching(platform.class))
        {
            y -= 140;
            velocity = -2;
        }    
        else if(!isTouching(platform.class))
        {
            velocity += fallSpeed;
            y+= velocity;
        }
        
        if(isTouching(enemy.class))
        {
            World world = getWorld();
            world.removeObject(this);
            Greenfoot.setWorld(new GameOver());
        }
        
        if(frameCount % 100 == 0)
        {
            World world = getWorld();
            Actor enemy = new enemy();
            world.addObject(enemy, 600, 285);
        }
        
        if(frameCount >= 400 && frameCount % 5 == 0 && Greenfoot.getRandomNumber(150)==1)
        {
            World world = getWorld();
            world.addObject(new enemy(),600,285);
        }
        
    }
    
    public void addedToWorld(World world)
    {
        x = getX();
        y = getY();
    }
}

