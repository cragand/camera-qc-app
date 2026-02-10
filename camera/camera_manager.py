"""Camera manager for discovering and managing multiple cameras."""
from typing import List, Optional
from .camera_interface import CameraInterface
from .opencv_camera import OpenCVCamera


class CameraManager:
    """Manages camera discovery and access."""
    
    @staticmethod
    def discover_cameras() -> List[CameraInterface]:
        """Discover all available cameras."""
        cameras = []
        
        # Discover OpenCV cameras (webcam, borescope)
        for i in range(5):  # Check first 5 indices
            cam = OpenCVCamera(i)
            if cam.open():
                cameras.append(cam)
            else:
                cam.close()
                break  # Stop when no more cameras found
        
        return cameras
    
    @staticmethod
    def get_camera_by_type(camera_type: str, index: int = 0) -> Optional[CameraInterface]:
        """Get a specific camera by type."""
        return OpenCVCamera(index)
