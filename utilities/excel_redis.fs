// Copyright (c) Jeremy Nelson, Colorado College
// Licensed under the GNU GENERAL PUBLIC LICENSE Version 3

open Microsoft.Office.Interop.Excel

open System
open System.Runtime.InteropServices
open NUnit.Framework


let app = new ApplicationClass(Visible = True)
let redis_server = new Redis()


