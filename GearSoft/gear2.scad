$fn=100;

    mod = 5;
    noTeeth = 25;
    widthfactor = 12;
    gearratio=2;

    module tooth(noTeeth,mod,widthfactor)
    {   pcd = noTeeth*mod;
    diamPitch = (3.14*pcd)/noTeeth;
    difference(){
        cube([2.2*mod,diamPitch/2,(widthfactor-1)*mod]);
        rotate([0,0,15])
        translate([1,-(diamPitch/2),-1])
        cube([2.2*mod,diamPitch/2,widthfactor*mod]);
        rotate([0,0,-15])
        translate([1,(diamPitch/2),-1])
        cube([2.2*mod,diamPitch/2,widthfactor*mod]);
    }
}


module gear(noTeeth,mod,widthfactor)
{
    pcd = noTeeth*mod;
    diamPitch = (3.14*pcd)/noTeeth;
    difference(){
    union(){
        cylinder(r=pcd/2,h=(widthfactor-1)*mod);
        for(i=[0:noTeeth])
        {
            rotate([0,0,(360/noTeeth)*i])
            translate([(pcd/2)-5,-(diamPitch/4),0])
            tooth(noTeeth,mod,widthfactor);
        }
    }
    translate([0,0,-1])
    cylinder(r=(0.3*pcd)/2,h=widthfactor*mod);
}
    
}

//tooth(20,7,12,1);
gear(noTeeth,mod,widthfactor);
centerdistance=mod*(gearratio+1)*(noTeeth/2);
translate([1,centerdistance,-1])

gear(noTeeth*gearratio,mod,widthfactor);