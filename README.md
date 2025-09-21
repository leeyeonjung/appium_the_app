# appium_the_app

## Version Information

- Python **3.13.7**
- appium **3.0.2**
- appium-python-client **5.2.4**
- uiautomator2 **5.0.1**
- pytest-check **2.5.3**
- pytest-html **4.1.1**
- numpy **2.3.3**
- pillow **11.3.0**

### Imaging Libraries
- imageio **2.37.0**  
  - 다양한 이미지 파일(GIF, PNG, JPG, TIFF 등) 읽기/쓰기 지원  
  - `scikit-image` 내부에서 이미지 파일 로딩에 사용
- lazy-loader **0.4**  
  - 모듈을 필요할 때만 메모리에 올리는 lazy loading 지원  
  - `scikit-image` 성능 최적화를 위해 필요
- networkx **3.5**  
  - 그래프 이론 기반 알고리즘 (nodes, edges, shortest path 등) 제공  
  - `scikit-image`의 그래프 기반 세그멘테이션 알고리즘에 사용
- scikit-image **0.25.2**  
  - 이미지 처리 라이브러리 (필터링, 변환, SSIM 등 제공)  
  - 예: `from skimage.metrics import structural_similarity`
- scipy **1.16.2**  
  - 수치/과학 계산 (선형대수, FFT, 신호처리 등)  
  - `scikit-image` 내부 연산에서 필요
- tifffile **2025.9.9**  
  - TIFF 포맷 이미지 읽기/쓰기 지원  
  - `scikit-image`가 TIFF 데이터 처리 시 사용

### Extra Packages
- PyWavelets **1.9.0**
- imagehash **4.3.2**