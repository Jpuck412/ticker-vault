export type QualityGrade="A"|"B"|"C"|"D";
export type Session="OVERNIGHT"|"PREMARKET"|"REGULAR"|"AFTER_HOURS";
export interface Big3Snapshot{ts:string;symbol:string;speedTradesSec:number;speedSharesSec:number;speedAccel:number;volumeSharesSec:number;volumeRatio:number;volumeAccel:number;spreadBps:number;spreadCompression:number;quoteRate:number;price:number;responseEfficiency:number;}
export interface Catalyst{symbol:string;publishedAt:string;type:string;source:string;verified:boolean;}
export interface Fingerprint{eventId:string;symbol:string;ignitionAt:string;session:Session;quality:QualityGrade;snapshots:Big3Snapshot[];catalyst?:Catalyst;}
