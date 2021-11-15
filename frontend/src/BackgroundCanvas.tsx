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
      const img1 = new Image();
      img1.src = 'pink-semicircle.png';
      console.log(width);
      img1.onload = () => {
        context.drawImage(
          img1,
          -50,
          -50,
          img1.height * (90 / width),
          img1.width * (90 / width)
        );
      };

      const img2 = new Image();
      img2.src = 'turq-hex.png';
      img2.onload = () => {
        context.drawImage(
          img2,
          width - 200,
          height - 200,
          250,
          (250 * img2.height) / img2.width
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
