/**
 * ──────────────────────────────────────────────────────
 * Playground Sound Engine
 * Synthesises smooth, musical UI sounds via Web Audio API.
 * No external audio files — just maths ✨
 * ──────────────────────────────────────────────────────
 */
const SFX = (() => {
  let ctx = null;
  let masterGain = null;
  let enabled = true;

  /** Lazily create AudioContext (must happen after user gesture) */
  function ensureCtx() {
    if (ctx) return true;
    try {
      ctx = new (window.AudioContext || window.webkitAudioContext)();
      masterGain = ctx.createGain();
      masterGain.gain.value = 0.35;          // keep volume pleasant
      masterGain.connect(ctx.destination);
      return true;
    } catch (e) { return false; }
  }

  /** Resume suspended context (browser autoplay policy) */
  function resume() {
    if (ctx && ctx.state === 'suspended') ctx.resume();
  }

  /* ── Primitive helpers ───────────────────────────── */

  /** Play a single sine/triangle tone that fades out */
  function tone(freq, duration = 0.12, type = 'sine', vol = 0.5, delay = 0) {
    if (!enabled || !ensureCtx()) return;
    resume();
    const t = ctx.currentTime + delay;
    const osc = ctx.createOscillator();
    const env = ctx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, t);
    env.gain.setValueAtTime(vol, t);
    env.gain.exponentialRampToValueAtTime(0.001, t + duration);
    osc.connect(env);
    env.connect(masterGain);
    osc.start(t);
    osc.stop(t + duration + 0.02);
  }

  /** Short noise burst (for percussive feel) */
  function noise(duration = 0.04, vol = 0.12) {
    if (!enabled || !ensureCtx()) return;
    resume();
    const t = ctx.currentTime;
    const size = ctx.sampleRate * duration;
    const buf = ctx.createBuffer(1, size, ctx.sampleRate);
    const data = buf.getChannelData(0);
    for (let i = 0; i < size; i++) data[i] = (Math.random() * 2 - 1) * vol;
    const src = ctx.createBufferSource();
    src.buffer = buf;
    const env = ctx.createGain();
    env.gain.setValueAtTime(vol, t);
    env.gain.exponentialRampToValueAtTime(0.001, t + duration);
    // Bandpass to make it softer
    const bpf = ctx.createBiquadFilter();
    bpf.type = 'bandpass';
    bpf.frequency.value = 4000;
    bpf.Q.value = 1.2;
    src.connect(bpf);
    bpf.connect(env);
    env.connect(masterGain);
    src.start(t);
    src.stop(t + duration + 0.01);
  }

  /* ── Public sound library ────────────────────────── */

  /** Soft click — for general UI taps, button presses */
  function click() {
    tone(880, 0.06, 'sine', 0.25);
    noise(0.025, 0.06);
  }

  /** Pop — slightly more musical, for placing letters */
  function pop() {
    tone(660, 0.08, 'sine', 0.3);
    tone(990, 0.06, 'triangle', 0.15, 0.02);
  }

  /** Slide — for puzzle tile movement */
  function slide() {
    tone(440, 0.1, 'triangle', 0.2);
    tone(520, 0.08, 'sine', 0.12, 0.03);
  }

  /** Backspace / undo — descending tone */
  function undo() {
    tone(520, 0.07, 'sine', 0.2);
    tone(390, 0.1, 'triangle', 0.18, 0.04);
  }

  /** Correct — bright ascending chime */
  function correct() {
    tone(523, 0.15, 'sine', 0.35);      // C5
    tone(659, 0.15, 'sine', 0.3, 0.08); // E5
    tone(784, 0.2, 'sine', 0.3, 0.16);  // G5
    tone(1047, 0.25, 'triangle', 0.2, 0.24); // C6
  }

  /** Error — gentle dissonant buzz */
  function error() {
    tone(220, 0.18, 'sawtooth', 0.12);
    tone(208, 0.18, 'sawtooth', 0.1, 0.02);
    noise(0.06, 0.08);
  }

  /** Win / celebration — full musical flourish */
  function win() {
    const notes = [523, 587, 659, 784, 880, 1047]; // C D E G A C
    notes.forEach((f, i) => {
      tone(f, 0.2, 'sine', 0.3, i * 0.09);
      tone(f * 1.5, 0.15, 'triangle', 0.1, i * 0.09 + 0.03);
    });
  }

  /** Hover — very subtle high-pitched tick */
  function hover() {
    tone(1200, 0.035, 'sine', 0.08);
  }

  /** Select / switch — two-note chirp */
  function select() {
    tone(600, 0.06, 'sine', 0.2);
    tone(800, 0.08, 'sine', 0.22, 0.05);
  }

  /** Hint — magical shimmer */
  function hint() {
    tone(880, 0.12, 'sine', 0.2);
    tone(1320, 0.1, 'triangle', 0.15, 0.04);
    tone(1760, 0.08, 'sine', 0.1, 0.08);
  }

  /** Toggle sound on/off */
  function toggle() {
    enabled = !enabled;
    return enabled;
  }

  return { click, pop, slide, undo, correct, error, win, hover, select, hint, toggle, get enabled() { return enabled; } };
})();
