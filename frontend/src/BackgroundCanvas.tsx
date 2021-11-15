import React, { useRef, useEffect } from 'react';

interface Props {
  width: number;
  height: number;
}

const BackgroundCanvas = ({ width, height }: Props) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    if (canvasRef.current) {
      const canvas = canvasRef.current;
      const context = canvas.getContext('2d');
      if (context == null) throw new Error('Could not get context');

      const scale = Math.min(width / 1100, 0.7);

      const img1 = new Image();
      img1.src = 'turq-hex.png';
      img1.onload = () => {
        context.drawImage(
          img1,
          -100,
          height - 100 - 350 * scale,
          (img1.width * scale) / 1.8,
          (img1.height * scale) / 1.8
        );
      };

      const img2 = new Image();
      img2.src = 'orange-circle.png';
      img2.onload = () => {
        context.drawImage(
          img2,
          width - 350 * scale,
          -100 + 80 * scale,
          (img2.width * scale) / 1.2,
          (img2.height * scale) / 1.2
        );
      };
    }
  }, []);

  return (
    <canvas
      ref={canvasRef}
      height={height}
      width={width}
      style={{ position: 'fixed', zIndex: -1, opacity: 0.8 }}
    />
  );
};

BackgroundCanvas.defaultProps = {
  width: window.innerWidth,
  height: window.innerHeight,
};

export default BackgroundCanvas;
