import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class enemy here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class enemy extends Actor
{
    /**
     * Act - do whatever the enemy wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void addScore()
    {
        MyWorld world = (MyWorld) getWorld();
        world.addCounter();
    }
    public void act() 
    {
        move(-3);
        
        if(getX() < 2)
        {
            addScore();
            getWorld().removeObject(this);
        }
    }    
}
