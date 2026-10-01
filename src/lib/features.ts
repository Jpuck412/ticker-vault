import {Big3Snapshot} from "./types";
export function pctChange(now:number,base:number){return base===0?0:(now-base)/Math.abs(base);}
export function spreadBps(bid:number,ask:number){const mid=(bid+ask)/2;return mid<=0?0:((ask-bid)/mid)*10_000;}
export function responseEfficiency(priceMovePct:number,dollarVolume:number){return dollarVolume<=0?0:priceMovePct/Math.log10(10+dollarVolume);}
export function big3Agreement(x:Big3Snapshot){return {speedUp:x.speedAccel>0,volumeUp:x.volumeAccel>0,spreadHealthy:x.spreadCompression>=0,all:x.speedAccel>0&&x.volumeAccel>0&&x.spreadCompression>=0};}
