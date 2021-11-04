import rhinoscriptsyntax as rs
import System, Rhino, scriptcontext


def ImportXYZRGB():
    #File open
    strPath=rs.OpenFileName("XYZRGB file to import", "XYZ Color files (*.xyz)|*.xyz")
    if not strPath: return
    file=open(strPath)
    if not file: return
    
    pc = Rhino.Geometry.PointCloud()
    num=0
    for line in file:
        num+=1
        if (num%1000)==0: print "Reading line %d K" %(num/1000)
        d=line.split()
        pt=Rhino.Geometry.Point3d(float(d[0]),float(d[1]),float(d[2]))
        try:
            col=System.Drawing.Color.FromArgb(int(d[3]),int(d[4]),int(d[5]))
        except LookupError:  #RGB absent in line
            col=System.Drawing.Color.FromArgb(0,0,0)
        pc.Add(pt,col)
    file.close()
    
    print "Done reading file, adding point cloud"
    obj=scriptcontext.doc.Objects.AddPointCloud(pc)
    scriptcontext.doc.Views.Redraw()
    
    
if __name__ == "__main__":
    ImportXYZRGB()