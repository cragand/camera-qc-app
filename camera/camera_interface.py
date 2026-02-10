"""Abstract camera interface for unified camera handling."""
from abc import ABC, abstractmethod
from typing import Optional, Tuple
import numpy as np


class CameraInterface(ABC):
    """Base class for all camera types."""
    
    def __init__(self, camera_id: str):
        self.camera_id = camera_id
        self.is_open = False
    
    @abstractmethod
    def open(self) -> bool:
        """Open camera connection. Returns True if successful."""
        pass
    
    @abstractmethod
    def close(self):
        """Close camera connection."""
        pass
    
    @abstractmethod
    def capture_frame(self) -> Optional[np.ndarray]:
        """Capture a single frame. Returns numpy array (BGR format) or None if failed."""
        pass
    
    @abstractmethod
    def get_resolution(self) -> Tuple[int, int]:
        """Get current resolution as (width, height)."""
        pass
    
    @abstractmethod
    def set_resolution(self, width: int, height: int) -> bool:
        """Set resolution. Returns True if successful."""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable camera name."""
        pass
