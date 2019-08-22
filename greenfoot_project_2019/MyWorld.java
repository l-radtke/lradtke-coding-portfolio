import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{
    int counter = 0;
    
    public void act()
    {
        showText(counter + "",10,10);
    }
    public void addCounter()
    {
        counter = counter + 1;
    }
    public int getCounter()
    {
        return counter;
    }
    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        prepare();
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        platform platform = new platform();
        addObject(platform,207,357);
        platform platform2 = new platform();
        addObject(platform2,488,356);
        player player = new player();
        addObject(player,77,302);
    }
}
