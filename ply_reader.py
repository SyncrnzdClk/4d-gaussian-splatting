from plyfile import PlyData, PlyElement
def fetch_ply(path):
    plydata = PlyData.read(path)
    vertices = plydata['vertex']
    print(vertices.data.dtype)
if __name__ == "__main__":
    fetch_ply("./gaussians.ply")
