#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 23:14:11 2025

@author: june-yay
"""
# fuelwave_site.py
import os
import webbrowser
import pathlib

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Fuelwave — Marine & Propane Refueling</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root{
      --navy:#0B1B2B; --navy-2:#12355B; --blood:#E63946; --aqua:#2EC4B6; --ink:#e6edf5;
      --muted:#9fb0c4; --line:rgba(255,255,255,.16); --bg:#0a1626;
      --glass-top:rgba(255,255,255,.06); --glass-bot:rgba(255,255,255,.02);
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    html{scroll-behavior:smooth}
    body{
      margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--ink);
      background:
        radial-gradient(1200px 600px at 10% -10%, #1b2e52 0%, transparent 60%),
        radial-gradient(900px 500px at 110% 10%, #0f2644 0%, transparent 55%),
        linear-gradient(180deg,#0c1a2d 0%, #081220 100%);
      background-color:var(--bg);
      scroll-snap-type:y proximity;
    }
    a{color:inherit}
    section{padding:70px 0; scroll-snap-align:start}
    .container{max-width:1160px;margin:0 auto;padding:0 24px}
    .btn{display:inline-flex;align-items:center;gap:10px;border-radius:9999px;padding:12px 18px;text-decoration:none;transition:.2s;border:0;font-weight:700;cursor:pointer;white-space:nowrap}
    .btn-primary{background:var(--blood);color:#fff;box-shadow:0 8px 24px rgba(230,57,70,.35)}
    .btn-primary:hover{filter:brightness(.95);transform:translateY(-1px)}
    .btn-outline{border:1px solid var(--line);color:#fff;background:transparent}
    .btn-outline:hover{background:rgba(255,255,255,.06)}
    .btn-app{background:linear-gradient(145deg,#38e0d2,#23bfb2);color:#06222a;box-shadow:0 8px 24px rgba(46,196,182,.35)}
    .btn-app:hover{filter:brightness(.98);transform:translateY(-1px)}
    .btn[disabled], .btn[aria-disabled="true"]{opacity:.55;cursor:not-allowed;transform:none;filter:none}
    /* Header + scroll progress */
    header{ position:sticky;top:0;z-index:60;background:rgba(9,17,29,.6);backdrop-filter:saturate(180%) blur(10px); border-bottom:1px solid var(--line) }
    header .row{height:68px;display:flex;align-items:center;justify-content:space-between;gap:12px}
    header a{color:var(--ink);text-decoration:none;opacity:.95}
    header a:hover{color:var(--blood)}
    nav{gap:20px;display:none}
    @media(min-width:900px){ nav{display:flex} }
    .brand{display:flex;align-items:center;gap:12px;color:#fff;text-decoration:none}
    .brand .logo{
      height:40px;width:40px;border-radius:12px;
      background:linear-gradient(145deg,var(--aqua),#1fb3a5);
      display:flex;align-items:center;justify-content:center;font-weight:900;color:#07131f;
      box-shadow:0 8px 24px rgba(46,196,182,.35);
    }
    .actions{display:flex;gap:10px;align-items:center}
    .progress{position:absolute; left:0; right:0; bottom:-1px; height:3px; background:rgba(255,255,255,.06)}
    .progress>span{display:block; height:100%; width:0%; background:linear-gradient(90deg, var(--aqua), #62f6ea); box-shadow:0 0 12px rgba(46,196,182,.45)}
    /* Sticky section titles */
    .sticky-head{position:sticky; top:68px; z-index:1; padding:8px 0 12px; background:transparent}
    .sticky-head h2{margin:0;font-size:28px}
    /* Hero */
    .hero{padding:86px 0;border-bottom:1px solid var(--line)}
    .hero h1{font-size:44px;line-height:1.06;margin:0}
    @media(min-width:640px){.hero h1{font-size:64px}}
    .tag{color:var(--aqua);font-weight:800;margin-top:10px;letter-spacing:.2px}
    .hero p{color:#cfe6ef;max-width:58ch}
    .panel{
      background:linear-gradient(180deg, var(--glass-top), var(--glass-bot));
      border:1px solid var(--line);border-radius:18px;padding:18px;
      box-shadow:0 18px 60px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.06)
    }
    .grid{display:grid;gap:22px}
    .g-2{grid-template-columns:1fr}
    .g-3{grid-template-columns:1fr}
    @media(min-width:860px){.g-2{grid-template-columns:1fr 1fr}.g-3{grid-template-columns:repeat(3,1fr)}}
    .center{text-align:center}
    .muted{color:var(--muted)}
    .card{background:linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.015));color:#eaf2f7;border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 12px 36px rgba(0,0,0,.35)}
    /* Pills */
    .pill{display:inline-block;padding:10px 16px;border-radius:9999px;border:1px solid var(--line);background:rgba(255,255,255,.03);cursor:pointer}
    .pill.active{background:linear-gradient(145deg,var(--navy-2),#0B1B2B);color:#eaf2f7;border-color:#2a415f}
    /* 3D selectable tiles */
    .select-tiles{display:grid;grid-template-columns:1fr;gap:16px;margin:14px 0}
    @media(min-width:700px){.select-tiles{grid-template-columns:repeat(2,1fr)}}
    /* ——— SMOOTH, GPU-FRIENDLY TILES ——— */
    .tile3d{position:relative;perspective:900px;transform-style:preserve-3d}
    .tile3d-inner{
      border-radius:18px;padding:18px;cursor:pointer;user-select:none;
      background:linear-gradient(180deg, rgba(255,255,255,.07), rgba(255,255,255,.03));
      border:1px solid var(--line);
      box-shadow:0 20px 60px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.06);
      transition:box-shadow .18s, border-color .18s, filter .18s;
      transform:translateZ(0) rotateX(0deg) rotateY(0deg);
      will-change: transform; backface-visibility: hidden; contain: paint; position:relative; overflow:hidden;
    }
    .tile3d-inner:hover{box-shadow:0 24px 80px rgba(0,0,0,.55)}
    .tile3d.selected .tile3d-inner{border-color:var(--aqua); box-shadow:0 0 0 2px rgba(46,196,182,.35), 0 24px 80px rgba(0,0,0,.55)}
    .tile3d-inner:active,.tile3d-inner.pressing{transform:translateZ(0) scale(.985)} /* smooth press */
    /* Ripple */
    .press-ripple{pointer-events:none; position:absolute; border-radius:9999px; transform:translate(-50%,-50%); opacity:.25; background:radial-gradient(circle, rgba(98,246,234,.6) 0%, rgba(98,246,234,0) 60%); animation:ripple .5s ease-out forwards;}
    @keyframes ripple{from{width:0;height:0;opacity:.35}to{width:220px;height:220px;opacity:0}}
    .tile-head{display:flex;align-items:center;gap:16px}
    /* Badges */
    .badge-3d{
      position:relative;width:74px;height:74px;border-radius:20px;flex:0 0 74px;display:grid;place-items:center;
      background: radial-gradient(120% 120% at 20% 15%, #ffffff 0%, #d7f5f4 16%, #50e3d6 38%, #1fb3a5 68%, #0b4258 100%);
      border:1px solid rgba(255,255,255,.5);
      box-shadow:inset 0 2px 8px rgba(0,0,0,.25), 0 12px 24px rgba(46,196,182,.35), 0 0 24px rgba(46,196,182,.20);
      overflow:hidden;
    }
    /* Minimal booking form */
    .panel-min{background:rgba(6,12,22,.35); border:1px solid var(--line); border-radius:16px; padding:16px}
    .form-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px}
    .form-title{font-weight:800;font-size:18px}
    .row{display:grid;gap:12px}
    @media(min-width:840px){.row-2{grid-template-columns:1fr 1fr}.row-3{grid-template-columns:repeat(3,1fr)}}
    .group{display:flex;flex-direction:column;gap:6px}
    label{font-size:13px;color:#c4d0de}
    .input{
      width:100%;border:1px solid rgba(255,255,255,.14);
      background:rgba(255,255,255,.03);color:#eaf2f7;border-radius:12px;padding:12px 13px;font-size:15px;
      transition:border-color .15s, box-shadow .15s, background .15s;
    }
    .input::placeholder{color:#96a8ba}
    .input:focus{outline:none;border-color:#5cded2;box-shadow:0 0 0 3px rgba(46,196,182,.25) inset;background:rgba(255,255,255,.05)}
    .checkline{display:flex;gap:10px;align-items:flex-start;color:#c9d6e3;font-size:14px}
    /* Chips/steppers */
    .chips{display:flex;flex-wrap:wrap;gap:8px}
    .chip{padding:8px 12px;border-radius:9999px;border:1px solid var(--line);cursor:pointer;background:rgba(255,255,255,.03);font-size:14px}
    .chip.active{border-color:#43d7ca; background:rgba(46,196,182,.12)}
    .stepper{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:10px;padding:6px 10px}
    .stepper button{background:transparent;border:0;color:#fff;font-size:16px;cursor:pointer}
    .stepper input{width:48px;background:transparent;border:0;color:#fff;text-align:center;font-size:14px}
    .section-grad{
      background:
        radial-gradient(700px 350px at 0% 20%, rgba(230,57,70,.10) 0%, transparent 70%),
        radial-gradient(700px 350px at 100% 80%, rgba(46,196,182,.12) 0%, transparent 70%);
    }
    .footer{background:rgba(6,12,22,.6);border-top:1px solid var(--line);padding:28px 0;text-align:center;color:#9fb0c4}
    /* Reveal on scroll */
    .reveal{opacity:0; transform:translateY(10px); transition:opacity .5s ease, transform .5s ease}
    .reveal.show{opacity:1; transform:none}
    /* Sponsor grid */
    .sponsor-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
    @media(min-width:760px){.sponsor-grid{grid-template-columns:repeat(4,1fr)}}
    .sponsor{
      display:flex;align-items:center;justify-content:center;height:52px;border-radius:12px;
      border:1px solid var(--line); background:rgba(255,255,255,.03); font-weight:700; color:#d6e5ef; cursor:pointer; transition:.18s; position:relative; overflow:hidden;
    }
    .sponsor:hover{transform:translateY(-1px)}
    .sponsor.selected{outline:2px solid var(--aqua); box-shadow:0 0 0 3px rgba(46,196,182,.28) inset}
    .sponsor:active,.sponsor.pressing{transform:scale(.985)}
    /* —— PULSE GLOW FOR PICK PROMPT (Step 1 tiles) —— */
    @keyframes fw-pulse {
      0% { box-shadow:0 0 0 0 rgba(98,246,234,.38), 0 0 24px rgba(98,246,234,.18) inset; border-color:rgba(98,246,234,.55) }
      60% { box-shadow:0 0 0 14px rgba(98,246,234,0), 0 0 24px rgba(98,246,234,.10) inset; border-color:rgba(98,246,234,.35) }
      100% { box-shadow:0 0 0 0 rgba(98,246,234,0), 0 0 24px rgba(98,246,234,.12) inset; border-color:rgba(98,246,234,.25) }
    }
    #step-service .tile3d-inner.pulse-glow{ animation: fw-pulse 1.6s ease-in-out infinite; }
  </style>
</head>
<body>
  <header>
    <div class="container row">
      <a class="brand" href="#" onclick="window.location.reload()">
        <div class="logo">FW</div>
        <div style="font-weight:800; font-size:18px">Fuelwave</div>
      </a>
      <nav>
        <a href="#services">Services</a>
        <a href="#how">How it works</a>
        <a href="#pricing">Pricing</a>
        <a href="#area">Service area</a>
        <a href="#book">Book</a>
        <a href="#contact">Contact</a>
      </nav>
      <div class="actions">
        <a class="btn btn-primary" href="#book">Book Now</a>
        <a class="btn btn-app" href="#" onclick="alert('App coming soon: iOS & Android');" title="iOS • Android">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="7" y="2" width="10" height="20" rx="2" stroke="#06222a" stroke-width="2"/>
            <circle cx="12" cy="18" r="1" fill="#06222a"/>
          </svg>
          Download App
        </a>
      </div>
      <div class="progress"><span id="progressBar"></span></div>
    </div>
  </header>

  <section class="hero">
    <div class="container grid g-2" style="align-items:center">
      <div class="panel reveal">
        <h1>On-Demand Marine & Propane Refueling</h1>
        <div class="tag">GTA • Dockside & Doorstep</div>
        <p style="margin-top:10px">Book a refuel in minutes. Licensed partners, transparent pricing, and flexible same-day windows when available.</p>
        <div style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn btn-primary" href="#book">Buy Fuel</a>
          <a class="btn btn-outline" href="#how">How it works</a>
        </div>
        <div style="display:flex;gap:8px;align-items:center;margin-top:14px">
          <span class="pill">Insured delivery</span>
          <span class="pill">Marine & Propane</span>
        </div>
      </div>

      <!-- Hero service tiles -->
      <div class="panel reveal">
        <div style="display:grid;gap:16px">
          <div class="tile3d" id="hero-marine">
            <div class="tile3d-inner service-tile" onmousemove="tilt(event,this)" onmouseleave="untilt(this)" data-service="Marine" onclick="toggleService('Marine')">
              <div class="tile-head">
                <div class="badge-3d">
                  <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
                    <path d="M3 14l9-4 9 4-3 1-6-2-6 2-3-1Z" fill="#1fb3a5"/>
                    <path d="M12 3l4 6H8l4-6Z" fill="#E63946"/>
                    <path d="M4 18c2 1 4 1 6 0s4-1 6 0 4 1 6 0v2c-2 1-4 1-6 0s-4-1-6 0-4 1-6 0v-2Z" fill="#0B1B2B"/>
                  </svg>
                </div>
                <div>
                  <div style="font-weight:900;font-size:18px">Refuel Boats</div>
                  <div class="muted" style="font-size:13px">Dockside gas/diesel at Port Credit & nearby marinas.</div>
                </div>
              </div>
            </div>
          </div>

          <div class="tile3d" id="hero-propane">
            <div class="tile3d-inner service-tile" onmousemove="tilt(event,this)" onmouseleave="untilt(this)" data-service="Propane" onclick="toggleService('Propane')">
              <div class="tile-head">
                <div class="badge-3d">
                  <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
                    <rect x="7" y="6" width="10" height="12" rx="3" fill="#1fb3a5"/>
                    <rect x="9" y="3" width="6" height="3" rx="1" fill="#E63946"/>
                    <rect x="10.5" y="2" width="3" height="2" rx=".6" fill="#0B1B2B"/>
                  </svg>
                </div>
                <div>
                  <div style="font-weight:900;font-size:18px">Propane Delivery</div>
                  <div class="muted" style="font-size:13px">Exchange/refill 20–100 lb cylinders; bulk on request.</div>
                </div>
              </div>
            </div>
          </div>
          <small id="helperTip" class="muted">Click a 3D tile to start. You’ll pick a sponsor/provider next.</small>
        </div>
      </div>
    </div>
  </section>

  <section id="services" class="section-grad">
    <div class="container">
      <div class="sticky-head"><h2>Why Fuelwave?</h2></div>
      <div class="grid g-3">
        <div class="card reveal"><div style="color:var(--aqua);font-weight:700">Licensed partners</div><div class="muted" style="font-size:14px">All deliveries performed by insured, licensed carriers.</div></div>
        <div class="card reveal"><div style="color:var(--aqua);font-weight:700">Same-day windows</div><div class="muted" style="font-size:14px">Request morning, afternoon, or evening slots.</div></div>
        <div class="card reveal"><div style="color:var(--aqua);font-weight:700">Transparent pricing</div><div class="muted" style="font-size:14px">Clear base fee + per-litre markup before you book.</div></div>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="container">
      <div class="sticky-head"><h2>How it Works</h2></div>
      <div class="grid g-3">
        <div class="card center reveal"><div class="btn btn-primary" style="padding:6px 10px;border-radius:9999px">1</div><div style="margin-top:8px;font-weight:700">Choose Service</div><div class="muted" style="font-size:14px">Boat fuel or Propane.</div></div>
        <div class="card center reveal"><div class="btn btn-primary" style="padding:6px 10px;border-radius:9999px">2</div><div style="margin-top:8px;font-weight:700">Pick Sponsor</div><div class="muted" style="font-size:14px">Select a preferred provider for your order.</div></div>
        <div class="card center reveal"><div class="btn btn-primary" style="padding:6px 10px;border-radius:9999px">3</div><div style="margin-top:8px;font-weight:700">Book & Refuel</div><div class="muted" style="font-size:14px">We schedule with the licensed partner; you get updates.</div></div>
      </div>
    </div>
  </section>

  <section id="pricing" class="section-grad">
    <div class="container">
      <div class="sticky-head"><h2>Pricing (pilot)</h2></div>
      <div class="grid g-2">
        <div class="card reveal"><div style="color:var(--blood);font-weight:700">Marine Fuel</div><div class="muted">Base fee: $25 per visit</div><div class="muted">Per-litre markup: $0.20/L over wholesale</div></div>
        <div class="card reveal"><div style="color:var(--blood);font-weight:700">Propane Exchange/Refill</div><div class="muted">20 lb: $29 • 30 lb: $39 • 40 lb: $49 • 100 lb: Quote</div><div class="muted">Bulk & commercial discounts available</div></div>
      </div>
    </div>
  </section>

  <section id="area">
    <div class="container">
      <div class="sticky-head"><h2>Service area</h2></div>
      <p class="muted reveal" style="max-width:70ch;margin:0 auto;text-align:center">
        Port Credit, Mississauga, and Etobicoke marinas. Propane coverage in Mississauga and nearby. If you’re outside this zone, submit a request and we’ll quote availability.
      </p>
    </div>
  </section>

  <section id="book" class="section-grad">
    <div class="container">
      <div class="sticky-head"><h2>Buy fuel / Book a refuel</h2></div>

      <!-- Step 1: Service -->
      <div class="panel reveal" id="step-service">
        <div style="display:flex;gap:10px;justify-content:center;margin-bottom:16px;flex-wrap:wrap">
          <button class="pill" id="pill-marine" onclick="setService('Marine')">Marine</button>
          <button class="pill" id="pill-propane" onclick="setService('Propane')">Propane</button>
        </div>

        <div class="select-tiles">
          <div class="tile3d" id="t-marine">
            <div class="tile3d-inner service-tile" onmousemove="tilt(event,this)" onmouseleave="untilt(this)" onclick="toggleService('Marine')" data-service="Marine">
              <div class="tile-head">
                <div class="badge-3d">
                  <svg width="36" height="36" viewBox="0 0 24 24" fill="none">
                    <path d="M3 14l9-4 9 4-3 1-6-2-6 2-3-1Z" fill="#1fb3a5"/>
                    <path d="M12 3l4 6H8l4-6Z" fill="#E63946"/>
                    <path d="M4 18c2 1 4 1 6 0s4-1 6 0 4 1 6 0v2c-2 1-4 1-6 0s-4-1-6 0-4 1-6 0v-2Z" fill="#0B1B2B"/>
                  </svg>
                </div>
                <div><div style="font-weight:900">Refuel Boats</div><div class="muted" style="font-size:13px">Gas/Diesel dockside</div></div>
              </div>
            </div>
          </div>

          <div class="tile3d" id="t-propane">
            <div class="tile3d-inner service-tile" onmousemove="tilt(event,this)" onmouseleave="untilt(this)" onclick="toggleService('Propane')" data-service="Propane">
              <div class="tile-head">
                <div class="badge-3d">
                  <svg width="36" height="36" viewBox="0 0 24 24" fill="none">
                    <rect x="7" y="6" width="10" height="12" rx="3" fill="#1fb3a5"/>
                    <rect x="9" y="3" width="6" height="3" rx="1" fill="#E63946"/>
                    <rect x="10.5" y="2" width="3" height="2" rx=".6" fill="#0B1B2B"/>
                  </svg>
                </div>
                <div><div style="font-weight:900">Propane Delivery</div><div class="muted" style="font-size:13px">20–100 lb • bulk</div></div>
              </div>
            </div>
          </div>
        </div>

        <div class="panel-min" id="quickDetails" style="margin-top:14px">
          <div class="form-head">
            <div class="form-title" id="qdTitle">Details</div>
            <div class="muted" style="font-size:12px">Tap to select; you can edit later</div>
          </div>

          <!-- Marine presets -->
          <div id="qdMarine" style="display:none">
            <div class="group">
              <label>Fuel type</label>
              <div class="chips" id="chipsFuelType">
                <span class="chip" data-value="Gasoline">Gasoline</span>
                <span class="chip" data-value="Diesel">Diesel</span>
              </div>
            </div>
            <div class="group" id="octaneRow" style="margin-top:8px; display:none">
              <label>Octane (Gasoline)</label>
              <div class="chips" id="chipsOctane">
                <span class="chip" data-value="87">87</span>
                <span class="chip" data-value="89">89</span>
                <span class="chip" data-value="91">91</span>
              </div>
            </div>
            <div class="group" style="margin-top:8px">
              <label>Estimated litres</label>
              <div class="chips" id="chipsLitres">
                <span class="chip" data-value="50L">50L</span>
                <span class="chip" data-value="100L">100L</span>
                <span class="chip" data-value="150L">150L</span>
                <span class="chip" data-value="200L+">200L+</span>
              </div>
            </div>
          </div>

          <!-- Propane presets -->
          <div id="qdPropane" style="display:none">
            <div class="group">
              <label>Cylinder size</label>
              <div class="chips" id="chipsSize">
                <span class="chip" data-value="20 lb">20 lb</span>
                <span class="chip" data-value="30 lb">30 lb</span>
                <span class="chip" data-value="40 lb">40 lb</span>
                <span class="chip" data-value="100 lb">100 lb</span>
              </div>
            </div>
            <div class="group" style="margin-top:8px">
              <label>Quantity</label>
              <div class="stepper">
                <button type="button" onclick="stepQty(-1)">-</button>
                <input id="qty" value="1" inputmode="numeric" pattern="[0-9]*">
                <button type="button" onclick="stepQty(1)">+</button>
              </div>
            </div>
          </div>

          <div class="group" style="margin-top:8px">
            <label for="f-details">Selected details</label>
            <input class="input" id="f-details" placeholder="(auto-filled from your selections)">
          </div>
        </div>

        <div style="text-align:right;margin-top:12px">
          <button class="btn btn-primary" onclick="goSponsors()">Next: Pick Sponsor</button>
        </div>
      </div>

      <!-- Step 2: Sponsor -->
      <div class="panel reveal" id="step-sponsor" style="display:none">
        <div class="sticky-head"><h2>Choose a Sponsor / Provider</h2></div>
        <div class="muted" style="margin-bottom:10px">We’ll match your request with your preferred provider (when available).</div>
        <div class="sponsor-grid" id="sponsorGrid"></div>
        <div style="display:flex;justify-content:space-between;margin-top:14px;gap:10px;flex-wrap:wrap">
          <button class="btn btn-outline" onclick="backToService()">Back</button>
          <button id="btnNextDetails" class="btn btn-primary" onclick="goForm()" disabled aria-disabled="true">Next: Details</button>
        </div>
      </div>

      <!-- Step 3: Booking Details -->
      <div class="panel-min reveal" id="step-form" style="display:none">
        <div class="form-head">
          <div class="form-title">Booking Details</div>
          <div class="muted" style="font-size:12px">We’ll confirm timing & price before dispatch</div>
        </div>
        <div class="row row-2">
          <div class="group">
            <label for="f-location">Location</label>
            <input class="input" id="f-location" list="suggestions" placeholder="Marina + Slip # or Address">
            <datalist id="suggestions">
              <option value="Port Credit Marina"><option value="Lakefront Promenade Marina">
              <option value="Credit Village Marina"><option value="Etobicoke Yacht Club">
              <option value="Humber Bay Park Marina">
            </datalist>
          </div>
          <div class="group">
            <label for="f-window">Preferred date & time window</label>
            <input class="input" id="f-window" placeholder="e.g., Tue 2–5pm">
          </div>
          <div class="group">
            <label for="f-details">Fuel / Propane details</label>
            <input class="input" id="f-details" placeholder="(auto-filled from your selections)">
          </div>
          <div class="group">
            <label for="f-access">Access notes</label>
            <input class="input" id="f-access" placeholder="Gate codes, dock instructions">
          </div>
        </div>
        <div class="row row-3" style="margin-top:6px">
          <div class="group"><label for="f-name">Name</label><input class="input" id="f-name" placeholder="Full name"></div>
          <div class="group"><label for="f-email">Email</label><input class="input" id="f-email" placeholder="you@email.com"></div>
          <div class="group"><label for="f-phone">Phone</label><input class="input" id="f-phone" placeholder="(xxx) xxx-xxxx"></div>
        </div>
        <div class="checkline" style="margin-top:8px">
          <input type="checkbox" id="f-perm" style="transform:translateY(2px)">
          <label for="f-perm" style="margin:0">I confirm I have permission for refueling at this location and will follow safety instructions.</label>
        </div>
        <div style="margin-top:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap">
          <button class="btn btn-primary" onclick="submitForm()">Submit request</button>
          <span class="notice" id="msg"></span>
        </div>
        <div class="notice" style="margin-top:8px" id="summary"></div>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="container center">
      <div class="sticky-head"><h2>Contact</h2></div>
      <div class="muted reveal">Phone: (XXX) XXX-XXXX • Email: hello@fuelwave.com</div>
      <div class="muted reveal" style="margin-top:6px">Base: Mississauga, ON</div>
    </div>
  </section>

  <footer class="footer">
    <div>© 2025 Fuelwave. All rights reserved.</div>
    <div style="max-width:70ch;margin:6px auto 0">Fuelwave is a booking platform. Refueling is performed by licensed carriers compliant with Ontario safety regulations.</div>
  </footer>

  <script>
    /* ---- 3D tilt (SPRING-SMOOTHED) ---- */
    const _tiltState = new WeakMap();
    function _clamp(n, min, max){ return Math.max(min, Math.min(max, n)); }
    function tilt(e, el){
      if(!_tiltState.has(el)){
        _tiltState.set(el, {rx:0, ry:0, tx:0, ty:0, vx:0, vy:0, raf:null, active:false});
      }
      const s = _tiltState.get(el);
      const r = el.getBoundingClientRect();
      const dx = _clamp((e.clientX - (r.left + r.width/2)) / (r.width/2), -1, 1);
      const dy = _clamp((e.clientY - (r.top + r.height/2)) / (r.height/2), -1, 1);
      s.tx = 6 * dx; s.ty = -5 * dy; s.active = true;
      if(!s.raf){
        const step = () => {
          const k = 0.22, d = 0.72; // stiffness, damping
          s.vy += (s.tx - s.ry) * k; s.vy *= d; s.ry += s.vy;
          s.vx += (s.ty - s.rx) * k; s.vx *= d; s.rx += s.vx;
          el.style.transform = `translateZ(0) rotateX(${s.rx.toFixed(2)}deg) rotateY(${s.ry.toFixed(2)}deg)`;
          const stillMoving = (Math.abs(s.vx) + Math.abs(s.vy)) > 0.01 || s.active;
          s.raf = stillMoving ? requestAnimationFrame(step) : null;
        };
        s.raf = requestAnimationFrame(step);
      }
    }
    function untilt(el){
      const s = _tiltState.get(el) || {rx:0, ry:0, tx:0, ty:0, vx:0, vy:0, raf:null, active:false};
      s.tx = 0; s.ty = 0; s.active = false;
      if(!s.raf){
        const step = () => {
          const k = 0.22, d = 0.72;
          s.vy += (s.tx - s.ry) * k; s.vy *= d; s.ry += s.vy;
          s.vx += (s.ty - s.rx) * k; s.vx *= d; s.rx += s.vx;
          el.style.transform = `translateZ(0) rotateX(${s.rx.toFixed(2)}deg) rotateY(${s.ry.toFixed(2)}deg)`;
          const stillMoving = (Math.abs(s.vx) + Math.abs(s.vy)) > 0.01;
          s.raf = stillMoving ? requestAnimationFrame(step) : null;
        };
        s.raf = requestAnimationFrame(step);
      }
    }

    /* Reliable press ripple */
    function pressStart(e){
      const el = e.currentTarget;
      el.setPointerCapture?.(e.pointerId);
      el.classList.add('pressing');
      const rp = document.createElement('span');
      rp.className = 'press-ripple';
      const rect = el.getBoundingClientRect();
      const x = ('touches' in e) ? e.touches[0].clientX : e.clientX;
      const y = ('touches' in e) ? e.touches[0].clientY : e.clientY;
      rp.style.left = (x - rect.left) + 'px';
      rp.style.top  = (y - rect.top ) + 'px';
      rp.style.willChange = 'transform, opacity';
      el.appendChild(rp);
      rp.getBoundingClientRect(); // force reflow
      setTimeout(()=>rp.remove(), 520);
    }
    function pressEnd(e){ e.currentTarget.classList.remove('pressing'); }
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.service-tile').forEach(t=>{
        t.addEventListener('pointerdown', pressStart, {passive:true});
        t.addEventListener('pointerup', pressEnd);
        t.addEventListener('pointerleave', pressEnd);
      });
    });

    /* Scroll progress + reveal */
    const pb = document.getElementById('progressBar');
    document.addEventListener('scroll', () => {
      const h = document.documentElement;
      const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight);
      pb.style.width = (scrolled*100).toFixed(1) + '%';
    });
    const io = new IntersectionObserver((entries)=>{
      for(const e of entries){ if(e.isIntersecting) e.target.classList.add('show'); }
    }, {threshold: .1});
    document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

    /* ---- State ---- */
    let currentService = null;
    let selectedSponsor = null;
    const chipsFuelType = () => Array.from(document.querySelectorAll('#chipsFuelType .chip'));
    const chipsOctane   = () => Array.from(document.querySelectorAll('#chipsOctane .chip'));
    const chipsLitres   = () => Array.from(document.querySelectorAll('#chipsLitres .chip'));
    const chipsSize     = () => Array.from(document.querySelectorAll('#chipsSize .chip'));

    function clearActive(list){ list.forEach(c=>c.classList.remove('active')); }
    function toggleChip(chip, group){
      if(chip.classList.contains('active')) chip.classList.remove('active');
      else { clearActive(group); chip.classList.add('active'); }
      syncDetailsField();
    }
    function stepQty(delta){
      const q = document.getElementById('qty');
      let v = parseInt(q.value||'1',10);
      v = Math.max(1, v + delta);
      q.value = v;
      syncDetailsField();
    }
    function showQuickDetails(){
      document.getElementById('quickDetails').style.display = 'block';
      const m = document.getElementById('qdMarine');
      const p = document.getElementById('qdPropane');
      const title = document.getElementById('qdTitle');
      if(currentService === 'Marine'){
        title.textContent = 'Boat Fuel — quick details';
        m.style.display='block'; p.style.display='none';
      }else if(currentService === 'Propane'){
        title.textContent = 'Propane — quick details';
        m.style.display='none'; p.style.display='block';
      }else{
        title.textContent = 'Details';
        m.style.display='none'; p.style.display='none';
      }
      syncDetailsField();
    }
    function syncDetailsField(){
      let text = '';
      if(currentService === 'Marine'){
        const ft = chipsFuelType().find(c=>c.classList.contains('active'))?.dataset.value || '';
        const oc = chipsOctane().find(c=>c.classList.contains('active'))?.dataset.value || '';
        const li = chipsLitres().find(c=>c.classList.contains('active'))?.dataset.value || '';
        text = `Marine - ${ft || 'Fuel'}${oc ? ' ('+oc+')' : ''}${li ? ' • '+li : ''}`;
      }else if(currentService === 'Propane'){
        const sz = chipsSize().find(c=>c.classList.contains('active'))?.dataset.value || '';
        const qty = document.getElementById('qty').value || '1';
        text = `Propane - ${qty} × ${sz || 'size'}`;
      }
      const field = document.getElementById('f-details');
      if(field) field.value = text;
      const oct = document.getElementById('octaneRow');
      const gasActive = chipsFuelType().find(c=>c.dataset.value==='Gasoline' && c.classList.contains('active'));
      if(oct) oct.style.display = (currentService==='Marine' && gasActive) ? 'block' : 'none';
    }

    /* —— Glow prompt control —— */
    function setPulseGlow(on){
      const m = document.querySelector('#t-marine .tile3d-inner');
      const p = document.querySelector('#t-propane .tile3d-inner');
      [m,p].forEach(el => { if(!el) return; el.classList.toggle('pulse-glow', !!on); });
    }
    function setService(s){
      currentService = s;
      document.getElementById("pill-marine").classList.toggle("active", s==="Marine");
      document.getElementById("pill-propane").classList.toggle("active", s==="Propane");
      document.getElementById("t-marine").classList.toggle("selected", s==="Marine");
      document.getElementById("t-propane").classList.toggle("selected", s==="Propane");
      const hm = document.getElementById("hero-marine");
      const hp = document.getElementById("hero-propane");
      if(hm && hp){ hm.classList.toggle("selected", s==="Marine"); hp.classList.toggle("selected", s==="Propane"); }
      document.getElementById('helperTip').style.display = 'none';
      setPulseGlow(false); // user made a choice
      showQuickDetails();
    }
    function toggleService(s){
      if(currentService === s){ currentService = null; } else{ currentService = s; }
      document.getElementById("pill-marine").classList.toggle("active", currentService==="Marine");
      document.getElementById("pill-propane").classList.toggle("active", currentService==="Propane");
      document.getElementById("t-marine").classList.toggle("selected", currentService==="Marine");
      document.getElementById("t-propane").classList.toggle("selected", currentService==="Propane");
      const hm = document.getElementById("hero-marine");
      const hp = document.getElementById("hero-propane");
      if(hm && hp){ hm.classList.toggle("selected", currentService==="Marine"); hp.classList.toggle("selected", currentService==="Propane"); }
      document.getElementById('helperTip').style.display = currentService ? 'none' : 'inline';
      setPulseGlow(!currentService); // glow only when nothing is selected
      showQuickDetails();
    }

    /* chip listeners */
    document.addEventListener('click', (e)=>{
      if(e.target.classList.contains('chip')){
        const group = Array.from(e.target.parentElement.children);
        toggleChip(e.target, group);
      }
    });

    /* Sponsors */
    const sponsors = [
      { id:"harbourFuel", name:"HarbourFuel", tag:"Marine",  cta:"Preferred marina partner" },
      { id:"propanePlus", name:"PropanePlus", tag:"Propane", cta:"Fast cylinder swap" },
      { id:"dockDirect",  name:"DockDirect",  tag:"Marine",  cta:"Same-day dockside" },
      { id:"blueFlame",   name:"BlueFlame",   tag:"Propane", cta:"Bulk & residential" },
      { id:"waveEnergy",  name:"WaveEnergy",  tag:"Marine",  cta:"Premium diesel" },
      { id:"tankSwift",   name:"TankSwift",   tag:"Propane", cta:"Commercial routes" },
      { id:"marinaGo",    name:"MarinaGo",    tag:"Marine",  cta:"Weekend coverage" },
      { id:"propaneHub",  name:"PropaneHub",  tag:"Propane", cta:"Multi-size exchange" }
    ];

    function goSponsors(){
      if(!currentService){
        alert("Pick Marine or Propane to continue.");
        return;
      }
      const grid = document.getElementById("sponsorGrid");
      grid.innerHTML = "";
      selectedSponsor = null;

      sponsors
        .filter(x => (currentService==="Marine" ? x.tag==="Marine" : x.tag==="Propane"))
        .forEach(sp => {
          const d = document.createElement('div');
          d.className = "sponsor";
          d.textContent = sp.name;
          d.title = sp.cta;

          d.addEventListener('pointerdown', (e)=>{
            d.classList.add('pressing');
            const rp = document.createElement('span');
            rp.className = 'press-ripple';
            const rect = d.getBoundingClientRect();
            const x = ('touches' in e) ? e.touches[0].clientX : e.clientX;
            const y = ('touches' in e) ? e.touches[0].clientY : e.clientY;
            rp.style.left = (x-rect.left)+'px';
            rp.style.top  = (y-rect.top)+'px';
            d.appendChild(rp);
            setTimeout(()=>rp.remove(), 520);
          }, {passive:true});
          d.addEventListener('pointerup', ()=>d.classList.remove('pressing'));
          d.addEventListener('pointerleave', ()=>d.classList.remove('pressing'));

          d.onclick = () => {
            Array.from(grid.children).forEach(c=>c.classList.remove('selected'));
            if(selectedSponsor === sp.name){ selectedSponsor = null; }
            else { d.classList.add('selected'); selectedSponsor = sp.name; }
            updateNextBtn();
          };
          grid.appendChild(d);
        });

      updateNextBtn();
      document.getElementById("step-service").style.display = "none";
      document.getElementById("step-sponsor").style.display = "block";
      document.getElementById("step-form").style.display = "none";
    }
    function updateNextBtn(){
      const btn = document.getElementById('btnNextDetails');
      const enabled = !!selectedSponsor;
      btn.disabled = !enabled;
      btn.setAttribute('aria-disabled', String(!enabled));
    }
    function backToService(){
      document.getElementById("step-service").style.display = "block";
      document.getElementById("step-sponsor").style.display = "none";
      document.getElementById("step-form").style.display = "none";
      setPulseGlow(!currentService); // if user cleared, glow resumes
    }
    function goForm(){
      if(!selectedSponsor){
        alert("Please select a sponsor/provider to continue.");
        return;
      }
      document.getElementById("step-service").style.display = "none";
      document.getElementById("step-sponsor").style.display = "none";
      document.getElementById("step-form").style.display = "block";
      document.getElementById("summary").textContent = "Summary — Service: " + (currentService||'') + " • Sponsor: " + selectedSponsor;
    }
    function submitForm(){
      const msg = document.getElementById("msg");
      const required = [["Location","f-location"],["Time window","f-window"],["Details","f-details"],["Name","f-name"],["Email","f-email"],["Phone","f-phone"]];
      for (const [label,id] of required){
        if(!document.getElementById(id).value.trim()){
          msg.textContent = label + " is required.";
          msg.style.color = "#ff9aa5";
          return;
        }
      }
      if(!document.getElementById("f-perm").checked){
        msg.textContent = "Please confirm permission checkbox.";
        msg.style.color = "#ff9aa5";
        return;
      }
      if(!selectedSponsor){
        msg.textContent = "Please pick a sponsor before submitting.";
        msg.style.color = "#ff9aa5";
        return;
      }
      msg.style.color = "#9ff0e8";
      msg.textContent = "Thanks! (Local preview only — hook this to Formspree/Stripe in production.)";
      alert("Submitted!\\nService: "+currentService+"\\nSponsor: "+selectedSponsor+"\\nDetails: "+document.getElementById('f-details').value);
    }

    // Start: details hidden + pulse glow ON to draw attention
    document.getElementById('quickDetails').style.display = 'none';
    setPulseGlow(true);

    /* Reduced motion: disable tilt if requested */
    const _prm = window.matchMedia?.('(prefers-reduced-motion: reduce)');
    if(_prm && _prm.matches){
      document.querySelectorAll('.tile3d-inner').forEach(el=>{
        el.onmousemove = null; el.onmouseleave = null; el.style.transform = 'translateZ(0)';
      });
      setPulseGlow(false); // keep UI calm
    }
  </script>
</body>
</html>
"""

def main():
    out_dir = pathlib.Path.cwd() / "fuelwave_preview_site"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(HTML, encoding="utf-8")
    webbrowser.open("file://" + str(out_file))

if __name__ == "__main__":
    main()
