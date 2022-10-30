import com.thomasdiewald.pixelflow.java.DwPixelFlow;
import com.thomasdiewald.pixelflow.java.fluid.DwFluid2D;
import java.util.Random;


DwFluid2D fluid;


PGraphics2D pg_fluid;

public void setup() {
  size(800, 800, P2D);

  DwPixelFlow context = new DwPixelFlow(this);


  fluid = new DwFluid2D(context, width, height, 1);


  fluid.param.dissipation_velocity = 0.70f;
  fluid.param.dissipation_density  = 0.99f;


  fluid.addCallback_FluiData(new  DwFluid2D.FluidData() {
    public void update(DwFluid2D fluid) {
      if (true) {
        Random rand = new Random(); //instance of random class
        int upperboundx = 800;
        int upperboundy = 800;

        int int_randomx = rand.nextInt(upperboundx);
        int int_randomy = 500+rand.nextInt(upperboundy);
        int int_randomvx = rand.nextInt(upperboundx);
        int int_randomvy = rand.nextInt(upperboundy);
        float px     = int_randomx;
        float py     = height-int_randomy;
        float vx     = (int_randomvx - int_randomx) * +15;
        float vy     = (int_randomvy - int_randomy) * -15;
        fluid.addVelocity(px, py, 14, vx, vy);
        fluid.addDensity (px, py, 20, 0.0f, 0.4f, 1.0f, 1.0f);
        fluid.addDensity (px, py, 8, 1.0f, 1.0f, 1.0f, 1.0f);
        fluid.addDensity (100,650,50, 1.0f,1.0f,1.0f, 1.0f);


      }
    }
  });

  pg_fluid = (PGraphics2D) createGraphics(width, height, P2D);
}


public void draw() { 
  fluid.update();


  pg_fluid.beginDraw();
  pg_fluid.background(0);
  pg_fluid.endDraw();

  
  fluid.renderFluidTextures(pg_fluid, 0);


  image(pg_fluid, 0, 0);
}
