# QA — new seven-slide build

Verified in Cloud Browser:
- Home renders, start enters design; color expansion and green selection update state.
- Camera tabs show MP and change specs. Removed every hotspot/leader. Tele compares software and optical sampling at matched 3x framing.
- Game button highlights Prime, Performance and Adreno blocks.
- Memory 4 apps fill initial RAM; fifth app triggers visible Full. Extended RAM creates 8 total slots, reserves dark storage strip; 8 apps load and all become disabled.
- Display shows resolution with (1.5K); tabs offer FPS 30 vs 60/120/144, manual start/stop, 1K vs 1.5K/2K, and pixel enlargement toggle.
- Desktop scene and 360/390/430-wide mobile harness visually inspected (camera/processor/memory and updated display FPS/resolution).
- Transition navigation tested across all seven slides. No slide or color autoplay.

Build: npm run build passes. Runtime assets packaged locally, including Thai font and library dependencies. Vite warnings for vendored classic scripts are expected; files copied unchanged to dist/vendor.

Not verified: actual Android/Termux/touch gestures/landscape; sustained performance; real WebGL shader/refraction (Cloud Browser WebGL is disabled); hardware benchmark or actual virtual-RAM behavior. Product claims use IN source, not confirmed Thai SKU.

Update 1.1: verified desktop design has no white rectangle, device silhouettes remain on gradient. Checked mobile 360 FPS, 390 resolution and 430 tele comparison. Build passes and CSS mask URL is rebased to ../assets/device-mask.svg for relative hosting.

Update 1.2: inspected new green and black alpha PNGs on the gradient in Cloud Browser. Verified zoom button starts animation (data-animating=true, initial renderedZoom 1.000) and reaches 3.000, with reverse button available. Build passes. PNG alpha range 0..255 confirmed for both assets.

Update 1.3: resolution-comparison tab replaced by bit depth; RGB counts calculated as 2^bits per channel and 2^(3*bits) combinations. No native 10-bit V80 claim. FPS and resolution spec retained. Build passes.
Verified 1.3 in Cloud Browser: 8↔10 and 6↔8 selectors update counts, gray toggle works; 360px mobile layout fits without overlapping navigation.
